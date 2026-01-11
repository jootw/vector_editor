class Serializable:
    def to_dict(self):
        return {
            "type": type(self).__name__,
            "module": self.__module__
        }

    @staticmethod
    def from_dict(serialized):
        pass
