from store.serializable import Serializable


class Point2f(Serializable):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def to_dict(self):
        return {
            "x": self._x,
            "y": self._y
        }

    @staticmethod
    def from_dict(serialized):
        return Point2f(serialized["x"], serialized["y"])
