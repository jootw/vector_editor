from tool.tool import Tool


class EllipseTool(Tool):
    def __init__(self, document, history_manager, canvas):
        super().__init__(document, history_manager, "ellipse")
        self._canvas = canvas
