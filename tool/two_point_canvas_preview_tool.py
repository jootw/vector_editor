from action.draw_shape_action import DrawShapeAction
from tool.canvas_preview_tool import CanvasPreviewTool


class TwoPointCanvasPreviewTool(CanvasPreviewTool):
    def __init__(self, document, history_manager, canvas, tool_id):
        super().__init__(document, history_manager, canvas, tool_id)
        self._canvas = canvas
        self._first_point = None

    def _get_shape(self, first_point, second_point):
        pass

    def handle_canvas_mouse_press(self, event):
        self._first_point = event.get_pos()

    def handle_canvas_mouse_release(self, event):
        self._history_manager.do(DrawShapeAction(
            self._document,
            self._get_shape(self._first_point, event.get_pos())
        ))
        self._first_point = None
        super()._set_preview(None)

    def handle_canvas_mouse_move(self, event):
        if self._first_point is not None:
            self._set_preview(self._get_shape(self._first_point, event.get_pos()))

    def deactivate(self):
        self._set_preview(None)
