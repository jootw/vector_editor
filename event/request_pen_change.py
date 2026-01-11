from event.event import Event


class RequestPenChangeEvent(Event):
    def __init__(self, pen):
        super().__init__()
        self._pen = pen

    def get_pen(self):
        return self._pen
