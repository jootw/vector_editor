import uuid

from PySide6.QtWidgets import QAbstractGraphicsShapeItem

from pen.pen import Pen
from store.serializable import Serializable


class Shape(Serializable):
    def __init__(self, shape_type, pen=Pen(), uid=None):
        super().__init__()
        self._uid = uid if uid else str(uuid.uuid4())
        self._pen = pen
        self._shape_type = shape_type

    def get_bounding_box(self):
        return self.to_qt_shape().boundingRect()

    def get_id(self):
        return self._uid

    def get_type(self):
        return self._shape_type

    def to_qt_shape(self):
        shape = self._to_qt_shape()
        shape.setPen(self._pen.to_qt_pen())
        return shape

    def _to_qt_shape(self):
        return QAbstractGraphicsShapeItem()

    def to_dict(self):
        return {
            "id": self._uid,
            "type": self._shape_type,
            "pen": Pen.to_dict(self._pen)
        }
