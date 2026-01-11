from event.event import Event


class ShapeRemoveEvent(Event):
    def __init__(self, shape):
        super().__init__()
        self._shape = shape

    def get_shape(self):
        return self._shape
