from event.shape_add import ShapeAddEvent
from event.shape_remove import ShapeRemoveEvent


class Document:
    def __init__(self, event_bus):
        self._shapes = []
        self._event_bus = event_bus

    def add_shape(self, shape):
        if shape not in self._shapes:
            self._shapes.append(shape)
            self._event_bus.call_event(ShapeAddEvent(shape))

    def remove_shape(self, shape):
        if shape in self._shapes:
            self._shapes.remove(shape)
            self._event_bus.call_event(ShapeRemoveEvent(shape))
