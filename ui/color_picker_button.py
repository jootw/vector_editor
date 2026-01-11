# gemini-3-pro

from PySide6.QtCore import Signal
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QPushButton, QColorDialog)


class ColorPickerButton(QPushButton):
    colorChanged = Signal(str)

    def __init__(self, color_hex, parent=None):
        super().__init__(parent)
        self._color = color_hex
        self.setText(color_hex)
        self.clicked.connect(self._open_dialog)
        # Устанавливаем только цвет фона, остальное - по умолчанию
        self._update_stylesheet()

    def _open_dialog(self):
        c = QColorDialog.getColor(QColor(self._color), self)
        if c.isValid():
            hex_color = c.name()
            self._color = hex_color
            self.setText(hex_color)
            self._update_stylesheet()
            self.colorChanged.emit(hex_color)

    def _update_stylesheet(self):
        # 1. Вычисляем контрастный цвет текста (черный или белый)
        bg_color = QColor(self._color)
        # Если яркость фона низкая (темный), текст белый. Иначе черный.
        text_color = "white" if bg_color.lightness() < 128 else "black"

        # 2. Применяем стиль
        # Важно: border: 1px solid ... заставляет Qt отключить нативную отрисовку,
        # благодаря чему background-color начинает работать.
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self._color};
                color: {text_color};
                border: 1px solid #555555;
                border-radius: 4px;
                padding: 5px;
            }}
            QPushButton:hover {{
                border: 1px solid white; /* Подсветка при наведении */
            }}
        """)
