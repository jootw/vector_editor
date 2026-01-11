from PySide6.QtWidgets import QPushButton

from event.request_tool_change import RequestToolChangeEvent
from event.tool_change import ToolChangeEvent


class ToolButton(QPushButton):
    def __init__(self, event_bus, tool_id, display_name):
        super().__init__(display_name)
        self._event_bus = event_bus
        self._tool_id = tool_id
        self._display_name = display_name
        self.setCheckable(True)
        self.clicked.connect(lambda: event_bus.call_event(RequestToolChangeEvent(self._tool_id)))

        self._event_bus.start_listening(ToolChangeEvent, self._handle_tool_change)

    def _handle_tool_change(self, event):
        self.setChecked(event.get_tool_id() == self._tool_id)
