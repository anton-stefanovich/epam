from random import randint

figures = {
    'queen': [
        # 0:
        [8, 5, 2],
        # 1:
        [2, 3, 4, 7, 5, 9],
        # 2:
        [1, 3, 5, 8, 0],
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


# 1   2   3
# 4   5   6
# 7   8   9
# *   0   #

def main():
    start_point = randint(0, 9)
    print('Start point: %s' % start_point)

    for figure in figures:
        seq = magic_func(
            [start_point],  # current array
            figure,         # current figure
            3,              # max path length
        )

        print('Figure: \'%s\', ways: %d' % (figure, len(seq)))

        # debug
        # for path in seq:
        #     print(path)


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


if __name__ == "__main__":
    main()
