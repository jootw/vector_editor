from PySide6.QtWidgets import QGraphicsLineItem

from pen.pen import Pen
from shape.point2f import Point2f
from shape.shape import Shape


class LineShape(Shape):
    def __init__(self, first_point, second_point, pen=Pen(), uid=None):
        super().__init__("line", pen, uid)
        self._first_point = first_point
        self._second_point = second_point

    def get_first_point(self):
        return self._first_point

    def get_second_point(self):
        return self._second_point

    def to_dict(self):
        serialized = super().to_dict()
        serialized["first_point"] = self._first_point.to_dict()
        serialized["second_point"] = self._second_point.to_dict()

    @staticmethod
    def from_dict(serialized):
        deserialized = super().from_dict(serialized)
        return LineShape(
            Point2f.from_dict(serialized["first_point"]),
            Point2f.from_dict(serialized["second_point"]),
            deserialized.get_pen(),
            deserialized.get_id()
        )

    def _to_qt_shape(self):
        return QGraphicsLineItem(
            self._first_point.get_x(), self._first_point.get_y(),
            self._second_point.get_x(), self._second_point.get_y()
        )
