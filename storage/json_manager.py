import json


class JsonManager:
    def __init__(self, file):
        self._file = file

    def save(self, data, indent=4) -> None:
        with open(self._file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent)

    def load(self):
        with open(self._file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
