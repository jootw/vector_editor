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
        self.setStyleSheet(f"background-color: {self._color};")

    def _open_dialog(self):
        c = QColorDialog.getColor(QColor(self._color), self)
        if c.isValid():
            hex_color = c.name()
            self._color = hex_color
            self.setText(hex_color)
            self.setStyleSheet(f"background-color: {self._color};")
            self.colorChanged.emit(hex_color)
