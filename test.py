from random import randint
from figure import *
from field import *
from point import *


# create field
def get_field():
    return Field(
        [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['*', '0', '#'],
        ]
    )


# rebuild available matrix for the field
def build_matrix(field, vectors, multipliable):
    available_matrix = list(range(10))

    for y in range(len(field.points)):
        for x in range(len(field.points[y])):
            point = Point(x, y)
            if not field.is_point_valid(point):
                continue

            available_points = []
            for vector in vectors:
                available_points.extend(
                    get_available_points(
                        field, Point(x, y), vector, multipliable))

            available_cells = []
            for point in available_points:
                available_cells.append(
                    int(field.point(point.x, point.y)))

            available_matrix[
                int(field.point(x, y))] = available_cells

    return available_matrix


# get available point from vector and multipliable property
# start from one point, return all available points
def get_available_points(field, point, offset, multipliable):
    new_point = point.next(offset)

    if not field.is_point_valid(new_point):
        return list()

    else:
        next_points = \
            get_available_points(
                field, new_point, offset, multipliable) \
            if multipliable else list()

        next_points.append(new_point)
        return next_points


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
    figures = Figure.get_known_figures()

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
