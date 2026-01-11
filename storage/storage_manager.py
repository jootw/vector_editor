from event.open_file_event import OpenFileEvent
from event.save_file_event import SaveFileEvent
from storage.deserializer import Deserializer
from storage.json_manager import JsonManager


class StorageManager:
    def __init__(self, event_bus, document):
        self._event_bus = event_bus
        self._document = document

        self._event_bus.start_listening(OpenFileEvent, self._handle_open_file)
        self._event_bus.start_listening(SaveFileEvent, self._handle_save_file)

    def _handle_open_file(self, event):
        json_manager = JsonManager(event.get_path())

        shapes = []
        for shape in json_manager.load()["shapes"]:
            shapes.append(Deserializer.deserialize(shape))

        self._document.set_shapes(shapes)

    def _handle_save_file(self, event):
        shapes = []
        for shape in self._document.get_shapes():
            shapes.append(shape.to_dict())

        json_manager = JsonManager(event.get_path())
        json_manager.save({"shapes": shapes})
