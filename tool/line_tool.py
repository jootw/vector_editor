from shape.line_shape import LineShape
from tool.two_point_canvas_preview_tool import TwoPointCanvasPreviewTool


class LineTool(TwoPointCanvasPreviewTool):
    def __init__(self, document, history_manager, canvas):
        super().__init__(document, history_manager, canvas, "line")

    def _get_shape(self, first_point, second_point):
        return LineShape(
            first_point, second_point
            # TODO
        )
