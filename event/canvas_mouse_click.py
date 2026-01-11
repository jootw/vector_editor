from event.event import Event
from shape.point2f import Point2f


class CanvasMousePressEvent(Event):
    def __init__(self, canvas, qt_event):
        super().__init__()
        self._canvas = canvas
        pos = canvas.mapToScene(qt_event.pos())
        self._pos = Point2f(pos.x(), pos.y())

    def get_pos(self):
        return self._pos
