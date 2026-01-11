from action.action import Action


class DrawShapeAction(Action):
    def __init__(self, document, shape):
        super().__init__()

        self._document = document
        self._shape = shape

    def redo(self):
        self._document.add_shape(self._shape)

    def undo(self):
        self._document.remove_shape(self._shape)
