from random import randint
from figure import *


def get_figures():
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


def get_field():
    return [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#'],
    ]


# rebuild available matrix for the field
def build_matrix(field, vectors, multipliable):
    available_matrix = list(range(10))

    for y in range(len(field)):
        for x in range(len(field[y])):
            point = (x, y)
            if not is_point_valid(field, point):
                continue

            available_points = []
            for vector in vectors:
                available_points.extend(
                    get_available_points(
                        field, (x, y), vector, multipliable))

            available_cells = []
            for point in available_points:
                available_cells.append(
                    int(field[point[1]][point[0]]))

            available_matrix[
                int(field[y][x])] = available_cells

    return available_matrix


# get available point from vector and multipliable property
# start from one point, return all available points
def get_available_points(field, point, vector, multipliable):
    new_point = get_next_point(point, vector)

    if not is_point_valid(field, new_point):
        return list()

    else:
        next_points = \
            get_available_points(
                field, new_point, vector, multipliable) \
            if multipliable else list()

        next_points.append(new_point)
        return next_points


# get one next point based on current point and vector
def get_next_point(point, vector):
    return (point[0] + vector[0],
            point[1] + vector[1])


# check point validity
def is_point_valid(field, point):
    x, y = point[0], point[1]

    return 0 <= y < len(field) \
        and 0 <= x < len(field[y]) \
        and field[y][x].isdigit()


# initial function for rebuild movements matrix
def generate_paths(field, figures):
    for figure in figures:
        figure.path_matrix = \
            build_matrix(
                field,
                figure.offset,
                figure.is_multipliable)

    print('=== Matrix rebuild completed ===')


# calculate all path for all available figures
def start(figures, start_point):
    print('Start point: %s' % start_point)

    for figure in figures:
        seq = magic_func(
            [start_point],  # current array
            figure,         # current figure
            7,              # max path length
        )

        print('Figure: \'%s\', ways: %d'
              % (figure.name, len(seq)))

        # debug
        # for path in seq:
        #     print(path)


# collecting all available path
# step by step (recursively)
def magic_func(current, figure, length):
    results = []
    for next_pos in figure.path_matrix[current[-1]]:
        sequence = current.copy()
        sequence.append(next_pos)

        results += (
            [sequence]
            if len(sequence) >= length
            else magic_func(sequence, figure, length))

    return results


def main():
    # get all known figures
    figures = get_figures()

    # get task field
    field = get_field()

    # build path matrix
    # for field for each figure
    generate_paths(field, figures)

    # generate random start point
    start_point = randint(0, 9)

    # launch path calculation
    # based on generated path matrix
    start(figures, start_point)


# enter point
if __name__ == "__main__":
    main()
