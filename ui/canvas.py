from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QAction, QPen
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene

from action.action_stack import ActionStack
from config import CANVAS_INITIAL_COLOR
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

# class VectorEditorCanvas(QGraphicsView):
#     def __init__(self, window):
#         super().__init__()
#
#         self._window = window
#         self._tool = None
#         self._actionStack = ActionStack()
#         self.color = CANVAS_INITIAL_COLOR
#
#         self._setupScene()
#         self._setupMenubar()
#         self._setupProperties()
#
#     def _setupScene(self):
#         self.scene = QGraphicsScene()
#         self.setScene(self.scene)
#         self.scene.setSceneRect(0, 0, 200, 200)
#
#     def _setupMenubar(self):
#         undoAction = QAction("Undo", self._window)
#         undoAction.setShortcut("Ctrl + Z")
#         undoAction.setStatusTip("Undo last change")
#         undoAction.triggered.connect(self._actionStack.undo)
#         redoAction = QAction("Redo", self._window)
#         redoAction.setShortcut("Ctrl + Shift + Z")
#         redoAction.setStatusTip("Redo last undo")
#         redoAction.triggered.connect(self._actionStack.redo)
#
#         menu = self._window.menubar.addMenu("&Canvas")
#         menu.addAction(undoAction)
#         menu.addAction(redoAction)
#
#     def _setupProperties(self):
#         self.setRenderHints(self.renderHints() | QPainter.RenderHint.Antialiasing)
#         self.setAlignment(Qt.AlignmentFlag.AlignCenter)
#
#         self.setMouseTracking(True)
#
#     def do(self, action):
#         self._actionStack.do(action)
#
#     def undo(self):
#         if self._tool.can_undo():
#             self._actionStack.undo()
#
#     def redo(self):
#         if self._tool.can_redo():
#             self._actionStack.redo()
#
#     def resizeEvent(self, event, /):
#         super().resizeEvent(event)
#         self.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
#
#     def setTool(self, tool):
#         if self._tool is not None:
#             self._tool.stop()
#         self._tool = tool
#
#     def setColor(self, color):
#         self._window.picker.setStyleSheet(f"background-color: {color.name()}")
#         self.color = color
#
#     def getPaintColor(self):
#         return self.color
#
#     def mousePressEvent(self, event, /):
#         if self._tool is not None:
#             self._tool.mousePressEvent(event)
#         super().mousePressEvent(event)
#
#     def mouseReleaseEvent(self, event, /):
#         if self._tool is not None:
#             self._tool.mouseReleaseEvent(event)
#         super().mouseReleaseEvent(event)
#
#     def mouseMoveEvent(self, event, /):
#         pos = self.mapToScene(event.pos())
#         x, y = pos.x(), pos.y()
#         self._window.statusBar().showMessage(f"Cursor pos: {int(x)} {int(y)}")
#         if self._tool is not None:
#             self._tool.mouseMoveEvent(event)
#         super().mouseMoveEvent(event)
#
#     def mouseDoubleClickEvent(self, event, /):
#         if self._tool is not None:
#             self._tool.mouseDoubleClickEvent(event)
#         super().mouseDoubleClickEvent(event)
