# gemini-3-pro

import re
from enum import Enum

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (QTreeWidget, QTreeWidgetItem, QSpinBox, QDoubleSpinBox, QLineEdit,
                               QCheckBox, QHeaderView, QComboBox)

from ui.color_picker_button import ColorPickerButton


class PropertyEditor(QTreeWidget):
    # Сигнал: при любом изменении возвращает ПОЛНЫЙ словарь
    dataChanged = Signal(dict)

    def __init__(self, data_dict, parent=None):
        super().__init__(parent)
        self._root_data = data_dict

        # Настройка колонок
        self.setColumnCount(2)
        self.setHeaderLabels(["Property", "Value"])
        self.header().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)

        # Строим дерево
        self._build_tree(self._root_data, self.invisibleRootItem())
        self.expandAll()

    def _build_tree(self, current_container, parent_item):
        """Рекурсивно проходит по словарю и создает виджеты."""

        # Определяем по чему итерироваться (словарь или список)
        if isinstance(current_container, dict):
            iterator = current_container.items()
        elif isinstance(current_container, list):
            iterator = enumerate(current_container)
        else:
            return

        for key, value in iterator:
            item = QTreeWidgetItem(parent_item)
            item.setText(0, str(key))

            # --- Ветка 1: Вложенные структуры ---
            if isinstance(value, (dict, list)):
                item.setText(1, f"({type(value).__name__})")
                # Рекурсивный вызов для вложенности
                self._build_tree(value, item)

            # --- Ветка 2: Значения (Примитивы и Enum) ---
            else:
                # Создаем замыкание (closure), чтобы сохранить ссылку на конкретное место в словаре
                def on_value_changed(new_val, container=current_container, k=key):
                    # 1. Пишем значение в словарь (in-place modification)
                    container[k] = new_val
                    # 2. Отправляем сигнал со всем словарем
                    self.dataChanged.emit(self._root_data)

                # Создаем подходящий виджет
                editor = self._create_editor(value, on_value_changed)

                if editor:
                    self.setItemWidget(item, 1, editor)
                else:
                    item.setText(1, str(value))

    def _create_editor(self, value, callback):
        """Фабрика виджетов на основе типа данных."""

        # A. ENUM (Создаем ComboBox)
        if isinstance(value, Enum):
            combo = QComboBox()
            enum_class = type(value)

            # Заполняем вариантами
            for member in enum_class:
                combo.addItem(member.name, userData=member)

            # Выставляем текущее значение
            combo.setCurrentText(value.name)

            # При изменении сохраняем СТРОКУ (имя Enum)
            def on_enum_change(index):
                callback(combo.itemData(index))  # txt будет равен, например, "SOLID"

            combo.currentIndexChanged.connect(on_enum_change)
            return combo

        # B. Bool (CheckBox)
        elif isinstance(value, bool):
            chk = QCheckBox()
            chk.setChecked(value)
            chk.toggled.connect(callback)
            return chk

        # C. Integer (SpinBox)
        elif isinstance(value, int):
            spin = QSpinBox()
            spin.setRange(0, 9999999)
            spin.setValue(value)
            spin.valueChanged.connect(callback)
            return spin

        # D. Float (DoubleSpinBox)
        elif isinstance(value, float):
            spin = QDoubleSpinBox()
            spin.setRange(0.0, 9999999.0)
            spin.setValue(value)
            spin.valueChanged.connect(callback)
            return spin

        # E. String (ColorPicker или LineEdit)
        elif isinstance(value, str):
            # Проверка регуляркой на HEX цвет (#FFF или #FFFFFF)
            if re.fullmatch(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value) or re.fullmatch(r'^#(?:[0-9a-fA-F]{4}){2}$', value):
                btn = ColorPickerButton(value)
                btn.colorChanged.connect(callback)
                return btn
            else:
                le = QLineEdit(value)
                le.textChanged.connect(callback)
                return le

        return None
