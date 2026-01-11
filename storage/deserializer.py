import sys


class Deserializer:
    @staticmethod
    def deserialize(data):
        module = sys.modules[data["module"]]
        clazz = getattr(module, data["type"])
        return clazz.from_dict(data)
