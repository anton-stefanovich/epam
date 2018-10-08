class Field:
    def __init__(self, points):
        self._points = points

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
            and self._points[point.y][point.x].isdigit()
