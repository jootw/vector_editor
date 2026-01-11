from event.canvas_mouse_click import CanvasMousePressEvent
from event.canvas_mouse_move import CanvasMouseMoveEvent
from event.canvas_mouse_release import CanvasMouseReleaseEvent
from event.request_tool_change import RequestToolChangeEvent
from event.tool_change import ToolChangeEvent


class ToolManager:
    def __init__(self, event_bus, tool_registry):
        self._current_tool = None
        self._event_bus = event_bus
        self._tool_registry = tool_registry

        self._event_bus.start_listening(RequestToolChangeEvent, self._handle_request_tool_change)
        self._event_bus.start_listening(CanvasMousePressEvent, self._handle_canvas_mouse_press)
        self._event_bus.start_listening(CanvasMouseReleaseEvent, self._handle_canvas_mouse_release)
        self._event_bus.start_listening(CanvasMouseMoveEvent, self._handle_canvas_mouse_move)

    def _handle_request_tool_change(self, event):
        tool_id = event.get_tool_id()
        if self._current_tool is None or self._current_tool.get_tool_id != tool_id:
            if self._current_tool is not None:
                self._current_tool.deactivate()
            self._current_tool = self._tool_registry.get(tool_id)
            if self._current_tool is not None:
                self._current_tool.activate()
            self._event_bus.call_event(ToolChangeEvent(tool_id))

    def _handle_canvas_mouse_press(self, event):
        if self._current_tool is not None:
            self._current_tool.handle_canvas_mouse_press(event)

    def _handle_canvas_mouse_release(self, event):
        if self._current_tool is not None:
            self._current_tool.handle_canvas_mouse_release(event)

    def _handle_canvas_mouse_move(self, event):
        if self._current_tool is not None:
            self._current_tool.handle_canvas_mouse_move(event)
