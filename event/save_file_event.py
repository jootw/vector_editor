from event.event import Event


class SaveFileEvent(Event):
    def __init__(self, path):
        super().__init__()
        self._path = path

    def get_path(self):
        return self._path
