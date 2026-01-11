from event.request_pen_change import RequestPenChangeEvent
from pen.pen import Pen


class PenManager:
    def __init__(self, event_bus):
        self._current_pen = Pen()
        self._event_bus = event_bus

        self._event_bus.start_listening(RequestPenChangeEvent, self._handle_request_pen_change)

    def get_pen(self):
        return self._current_pen

    def _handle_request_pen_change(self, event):
        self._current_pen = Pen.from_dict(event.get_pen())
