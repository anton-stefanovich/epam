from random import randint

figures_next = {
    'bishop': {
        'vectors': [
            (1, 1), (-1, -1),
            (1, -1), (-1, 1)],
        'multipliable': True,
    },

    'rook': {
        'vectors': [
            (1, 0), (-1, 0),
            (0, 1), (0, -1)],
        'multipliable': True,
    },

    'knight': {
        'vectors': [
            (2, 1), (2, -1),
            (-2, 1), (-2, -1),
            (1, 2), (1, -2),
            (-1, 2), (-1, -2)],
        'multipliable': False,
    },

    'king': {
        'vectors': [
            (1, 0), (-1, 0),
            (0, 1), (0, -1),
            (1, 1), (-1, -1),
            (-1, 1), (1, -1)],
        'multipliable': False,
    },

    'queen': {
        'vectors': [
            (1, 0), (-1, 0),
            (0, 1), (0, -1),
            (1, 1), (-1, -1),
            (-1, 1), (1, -1)],
        'multipliable': True,
    },
}

figures = {
    'queen': [
        # 0:
        [8, 5, 2],
        # [7, 9, 8, 5, 2],
        # 1:
        [2, 3, 4, 7, 5, 9],
        # 2:
        [1, 3, 5, 8, 0],
        # [1, 3, 5, 8, 0, 4, 6],
        # 3:
        [2, 1, 6, 9, 5, 7],
        # 4:
        [1, 2, 5, 6, 8, 7],
        # 5:
        [1, 2, 3, 4, 6, 7, 8, 0, 9],
        # 6:
        [3, 2, 5, 4, 8, 9],
        # 7:
        [4, 1, 5, 3, 8, 9, 0],
        # 8:
        [7, 4, 5, 2, 6, 9, 0],
        # 9:
        [8, 7, 5, 1, 6, 3, 0],
    ],

    'king': [
        # 0:
        [7, 8, 9],
        # 1:
        [2, 5, 4],
        # 2:
        [1, 4, 5, 6, 3],
        # 3:
        [2, 5, 6],
        # 4:
        [1, 2, 5, 8, 7],
        # 5:
        [1, 2, 3, 4, 6, 7, 8, 9],
        # 6:
        [3, 2, 5, 8, 9],
        # 7:
        [4, 5, 8, 0],
        # 8:
        [4, 5, 6, 7, 9, 0],
        # 9:
        [6, 5, 8, 0],
    ]
}


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


# 1   2   3
# 4   5   6
# 7   8   9
# *   0   #

# initial function for rebuild movements matrix
def rebuild_matrix():
    figures.clear()  # !!!!!!!!!

    field = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#'],
    ]

    for figure in figures_next:
        figures[figure] = \
            build_matrix(
                field,
                figures_next.get(figure).get('vectors'),
                figures_next.get(figure).get('multipliable'))

    print('=== Matrix rebuild completed ===')


# calculate all path for all available figures
def main(start_point):
    print('Start point: %s' % start_point)

    for figure in figures:
        seq = magic_func(
            [start_point],  # current array
            figure,         # current figure
            7,              # max path length
        )

        print('Figure: \'%s\', ways: %d' % (figure, len(seq)))

        # debug
        # for path in seq:
        #     print(path)


# collecting all available path
# step by step (recursively)
def magic_func(current, figure, length):
    results = []
    for next_pos in figures.get(figure)[current[-1]]:
        sequence = current.copy()
        sequence.append(next_pos)

        results += (
            [sequence]
            if len(sequence) >= length
            else magic_func(sequence, figure, length))

    return results


# enter point
if __name__ == "__main__":
    # generate random start point
    start_here = randint(0, 9)

    # launch path calculation
    # based on manual path matrix
    main(start_here)

    # rebuilding path matrix
    rebuild_matrix()

    # launch path calculation
    # based on generated path matrix
    main(start_here)
