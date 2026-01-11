from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene

from event.canvas_mouse_click import CanvasMousePressEvent
from event.canvas_mouse_move import CanvasMouseMoveEvent
from event.canvas_mouse_release import CanvasMouseReleaseEvent
from event.shape_add import ShapeAddEvent
from event.shape_remove import ShapeRemoveEvent


class VectorCanvas(QGraphicsView):
    def __init__(self, event_bus):
        super().__init__()
        self._event_bus = event_bus

        self._drawn_shapes = []
        self._shape_to_qt = {}

        self._setup_properties()
        self._setup_scene()

        self._event_bus.start_listening(ShapeAddEvent, self._handle_shape_add)
        self._event_bus.start_listening(ShapeRemoveEvent, self._handle_shape_remove)

    def _setup_properties(self):
        self.setStyleSheet("background-color: white; border: 2px solid gray;")
        self.setRenderHints(self.renderHints() | QPainter.RenderHint.Antialiasing)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setMouseTracking(True)

    def _setup_scene(self):
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.scene.setSceneRect(0, 0, 200, 200)

    def add_shape(self, shape):
        qt_shape = shape.to_qt_shape()
        self.scene.addItem(qt_shape)
        self._drawn_shapes.append(shape)
        self._shape_to_qt[shape.get_id()] = qt_shape

    def remove_shape(self, shape):
        qt_shape = self._shape_to_qt[shape.get_id()]
        self.scene.removeItem(qt_shape)
        self._drawn_shapes.remove(shape)
        self._shape_to_qt.pop(shape.get_id())

    def resizeEvent(self, event, /):
        super().resizeEvent(event)
        self.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

    def mousePressEvent(self, event, /):
        self._event_bus.call_event(CanvasMousePressEvent(self, event))
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event, /):
        self._event_bus.call_event(CanvasMouseReleaseEvent(self, event))
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event, /):
        self._event_bus.call_event(CanvasMouseMoveEvent(self, event))
        super().mousePressEvent(event)

    def _handle_shape_add(self, event):
        self.add_shape(event.get_shape())

    def _handle_shape_remove(self, event):
        self.remove_shape(event.get_shape())
