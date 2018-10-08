class Figure:

    def __init__(self, name, offset, is_multipliable):
        self._name = name
        self._offset = offset
        self._is_multipliable = is_multipliable

        # empty path_matrix on initial state
        self.path_matrix = list()

    @property
    def name(self):
        return self._name

    @property
    def offset(self):
        return self._offset

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
                offset=[
                    (1, 1), (-1, -1),
                    (1, -1), (-1, 1)],
                is_multipliable=True),

            Figure(
                name='rook',
                offset=[
                    (1, 0), (-1, 0),
                    (0, 1), (0, -1)],
                is_multipliable=True),

            Figure(
                name='knight',
                offset=[
                    (2, 1), (2, -1),
                    (-2, 1), (-2, -1),
                    (1, 2), (1, -2),
                    (-1, 2), (-1, -2)],
                is_multipliable=False),

            Figure(
                name='king',
                offset=[
                    (1, 0), (-1, 0),
                    (0, 1), (0, -1),
                    (1, 1), (-1, -1),
                    (-1, 1), (1, -1)],
                is_multipliable=False),

            Figure(
                name='queen',
                offset=[
                    (1, 0), (-1, 0),
                    (0, 1), (0, -1),
                    (1, 1), (-1, -1),
                    (-1, 1), (1, -1)],
                is_multipliable=True),
        ]
