from action.action_stack import ActionStack
from event.request_redo_event import RequestRedoEvent
from event.request_undo_event import RequestUndoEvent


class HistoryManager(ActionStack):
    def __init__(self, event_bus, tool_manager):
        super().__init__()
        self._event_bus = event_bus
        self._tool_manager = tool_manager

        self._event_bus.start_listening(RequestUndoEvent, lambda event: self.undo())
        self._event_bus.start_listening(RequestRedoEvent, lambda event: self.redo())

    def undo(self):
        if self._tool_manager.can_undo():
            super().undo()

    def redo(self):
        if self._tool_manager.can_redo():
            super().redo()
