from PySide6.QtWidgets import QApplication

from action.action_stack import ActionStack
from document import Document
from event.event_bus import EventBus
from registry import Registry
from tool.ellipse_tool import EllipseTool
from tool.line_tool import LineTool
from tool.rect_tool import RectTool
from tool.tool_manager import ToolManager
from ui.canvas import VectorCanvas
from ui.window import VectorEditorWindow


class VectorEditor(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.setStyle("Fusion")

        self._event_bus = EventBus()
        self._document = Document(self._event_bus)
        self._history_manager = ActionStack()

        self._canvas = VectorCanvas(self._event_bus)
        self._window = VectorEditorWindow(self._event_bus, self._canvas)

        self._tool_registry = Registry()
        self._tool_registry.register("line", LineTool(self._document, self._history_manager, self._canvas))
        self._tool_registry.register("rect", RectTool(self._document, self._history_manager, self._canvas))
        self._tool_registry.register("ellipse", EllipseTool(self._document, self._history_manager, self._canvas))

        self._tool_manager = ToolManager(self._event_bus, self._tool_registry)

        self._window.show()
