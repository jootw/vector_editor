from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QColor

from shape.pen_style import PenStyle
from store.serializable import Serializable


class Pen(Serializable):
    def __init__(self, color="#000000", width=1.0, style=PenStyle["SolidLine"]):
        self._color = color
        self._width = width
        self._style = style

    def get_color(self):
        return self._color

    def get_width(self):
        return self._width

    def get_style(self):
        return self._style

    def to_qt_pen(self):
        pen = QPen()
        pen.setColor(QColor(self._color))
        pen.setWidthF(self._width)
        pen.setStyle(Qt.PenStyle[self._style.name])
        return pen

    def to_dict(self):
        return {
            "color": self.get_color(),
            "width": self.get_width(),
            "style": self.get_style()
        }

    @staticmethod
    def from_dict(serialized):
        return Pen(
            serialized["color"],
            serialized["width"],
            PenStyle[serialized["style"]]
        )
