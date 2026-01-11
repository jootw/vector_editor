from shape.rect_shape import RectShape
from tool.two_point_canvas_preview_tool import TwoPointCanvasPreviewTool


class RectTool(TwoPointCanvasPreviewTool):
    def __init__(self, document, history_manager, canvas, pen_manager):
        super().__init__(document, history_manager, canvas, pen_manager, "rect")
        self._canvas = canvas

    def _get_shape(self, first_point, second_point):
        return RectShape(
            first_point, second_point,
            self._pen_manager.get_pen()
        )
