from tool.tool import Tool


class CanvasPreviewTool(Tool):
    def __init__(self, document, history_manager, canvas, pen_manager, tool_id):
        super().__init__(document, history_manager, tool_id)
        self._canvas = canvas
        self._pen_manager = pen_manager
        self._preview_shape = None

    def _set_preview(self, shape):
        qt_shape = shape.to_qt_shape() if shape is not None else None
        if self._preview_shape is not None:
            self._canvas.scene.removeItem(self._preview_shape)
        self._preview_shape = qt_shape
        if self._preview_shape is not None:
            self._canvas.scene.addItem(self._preview_shape)
