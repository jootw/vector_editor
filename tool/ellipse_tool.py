from shape.ellipse_shape import EllipseShape
from tool.two_point_canvas_preview_tool import TwoPointCanvasPreviewTool


class EllipseTool(TwoPointCanvasPreviewTool):
    def __init__(self, document, history_manager, canvas):
        super().__init__(document, history_manager, canvas, "ellipse")
        self._canvas = canvas

    def _get_shape(self, first_point, second_point):
        return EllipseShape(
            first_point, second_point
            # TODO
        )
