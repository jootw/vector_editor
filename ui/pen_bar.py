from event.request_pen_change import RequestPenChangeEvent
from pen.pen import Pen
from ui.property_editor import PropertyEditor


class PenBar(PropertyEditor):
    def __init__(self, event_bus):
        super().__init__(Pen().to_tree_data())
        self._event_bus = event_bus
        self.dataChanged.connect(lambda pen_data: self._event_bus.call_event(
            RequestPenChangeEvent(pen_data)
        ))
