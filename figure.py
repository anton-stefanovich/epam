from point import Offset


class Figure:

    def __init__(self, name, offsets, is_multipliable):
        self._name = name
        self._offsets = offsets
        self._is_multipliable = is_multipliable

        # empty path_matrix on initial state
        self.path_matrix = list()

    @property
    def name(self):
        return self._name

    @property
    def offset(self):
        return self._offsets

    @property
    def is_multipliable(self):
        return self._is_multipliable

    @property
    def path_matrix(self):
        return self._path_matrix

    @path_matrix.setter
    def path_matrix(self, path_matrix: list):
        self._path_matrix = path_matrix

    @staticmethod
    def get_known_figures():
        return [
            Figure(
                name='bishop',
                offsets=[
                    Offset(1, 1),
                    Offset(1, -1),
                    Offset(-1, 1),
                    Offset(-1, -1)],
                is_multipliable=True),

            Figure(
                name='rook',
                offsets=[
                    Offset(1, 0),
                    Offset(0, 1),
                    Offset(-1, 0),
                    Offset(0, -1)],
                is_multipliable=True),

            Figure(
                name='knight',
                offsets=[
                    Offset(2, 1),
                    Offset(1, 2),
                    Offset(1, -2),
                    Offset(2, -1),
                    Offset(-1, 2),
                    Offset(-2, 1),
                    Offset(-2, -1),
                    Offset(-1, -2)],
                is_multipliable=False),

            Figure(
                name='king',
                offsets=[
                    Offset(1, 0),
                    Offset(0, 1),
                    Offset(0, 1),
                    Offset(1, 1),
                    Offset(-1, 0),
                    Offset(-1, 1),
                    Offset(1, -1),
                    Offset(-1, -1)],
                is_multipliable=False),

            Figure(
                name='queen',
                offsets=[
                    Offset(1, 0),
                    Offset(0, 1),
                    Offset(1, 1),
                    Offset(0, -1),
                    Offset(-1, 0),
                    Offset(1, -1),
                    Offset(-1, 1),
                    Offset(-1, -1)],
                is_multipliable=True),
        ]
