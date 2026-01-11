class Registry:
    def __init__(self):
        self._registry = {}

    def register(self, key, item):
        if key not in self._registry:
            self._registry[key] = item

    def get(self, key):
        if key in self._registry:
            return self._registry[key]
        return None
