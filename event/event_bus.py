
class EventBus:
    def __init__(self):
        self._listeners = {}

    def call_event(self, event):
        if event.__class__ not in self._listeners:
            return
        for listener in self._listeners[event.__class__]:
            listener(event)

    def start_listening(self, event_class, listener):
        if event_class not in self._listeners:
            self._listeners[event_class] = []
        self._listeners[event_class].append(listener)

    def stop_listening(self, event_class, listener):
        if event_class not in self._listeners:
            self._listeners[event_class] = []
        self._listeners[event_class].remove(listener)
