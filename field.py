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
        x, y = point[0], point[1]

        return 0 <= y < len(self._points) \
            and 0 <= x < len(self._points[y]) \
            and self._points[y][x].isdigit()
