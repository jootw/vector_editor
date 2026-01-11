from event.event import Event


class ToolChangeEvent(Event):
    def __init__(self, tool_id):
        super().__init__()
        self._tool_id = tool_id

    def get_tool_id(self):
        return self._tool_id
