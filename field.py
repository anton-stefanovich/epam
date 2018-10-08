class Field:
    def __init__(self, points):
        self._points = points

    @property
    def points(self):
        return self._points

    def point(self, x, y):
        return self._points[y][x] if \
            y < len(self._points) and \
            x < len(self._points[y]) else None

    def is_point_valid(self, point):
        return 0 <= point.y < len(self._points) \
            and 0 <= point.x < len(self._points[point.y]) \
            and self._points[point.y][point.x].isdigit()
