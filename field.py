from random import choice
from point import Point


class Field:
    def __init__(self, points, func):
        self._points = points
        self._func = func

    @property
    def points(self):
        return self._points

    def point(self, point):
        return self._points[point.y][point.x] if \
            point.y < len(self._points) and \
            point.x < len(self._points[point.y]) else None

    def is_point_valid(self, point):
        return 0 <= point.y < len(self._points) \
            and 0 <= point.x < len(self._points[point.y]) \
            and self._func(self._points[point.y][point.x])

    def random_point(self):
        rand_y = choice(range(len(self._points)))
        rand_x = choice(range(len(self._points[rand_y])))
        return self.point(Point(rand_x, rand_y))
