
class Tool:
    def __init__(self, document, history_manager, tool_id):
        self._document = document
        self._history_manager = history_manager
        self._tool_id = tool_id

    def activate(self):
        pass

    def deactivate(self):
        pass

    def can_undo(self):
        return True

    def can_redo(self):
        return True

    def get_tool_id(self):
        return self._tool_id

    def handle_canvas_mouse_press(self, event):
        pass

    def handle_canvas_mouse_release(self, event):
        pass

    def handle_canvas_mouse_move(self, event):
        pass
