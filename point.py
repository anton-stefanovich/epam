import copy


class Coord:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Offset(Coord):
    def __init__(self, x, y):
        super().__init__(x, y)


class Point(Coord):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    def move(self, offset):
        self._x = self.x + offset.x
        self._y = self.y + offset.y

    def next(self, offset=Offset(0, 0)):
        new_point = copy.deepcopy(self)
        new_point.move(offset)
        return new_point
