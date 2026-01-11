from PySide6.QtWidgets import QApplication

from document import Document
from event.event_bus import EventBus
from event.open_file_event import OpenFileEvent
from history_manager import HistoryManager
from pen.pen_manager import PenManager
from registry import Registry
from storage.storage_manager import StorageManager
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

        self._canvas = VectorCanvas(self._event_bus)
        self._window = VectorEditorWindow(self._event_bus, self._canvas)

        self._pen_manager = PenManager(self._event_bus)

        self._tool_registry = Registry()
        self._tool_manager = ToolManager(self._event_bus, self._tool_registry)
        self._history_manager = HistoryManager(self._event_bus, self._tool_manager)

        self._tool_registry.register("line", LineTool(
            self._document, self._history_manager,
            self._canvas, self._pen_manager
        ))
        self._tool_registry.register("rect", RectTool(
            self._document, self._history_manager,
            self._canvas, self._pen_manager
        ))
        self._tool_registry.register("ellipse", EllipseTool(
            self._document, self._history_manager,
            self._canvas, self._pen_manager
        ))

        self._storage_manager = StorageManager(self._event_bus, self._document)

        if len(args) > 1:
            self._event_bus.call_event(OpenFileEvent(args[1]))

        self._window.show()
