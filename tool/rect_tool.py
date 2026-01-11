from tool.tool import Tool


class RectTool(Tool):
    def __init__(self, document, history_manager, canvas):
        super().__init__(document, history_manager, "rect")
        self._canvas = canvas
