import re


def get_input(filename):
    with open(filename) as f:
        dots, folds = f.read().split('\n\n')
        dots_list = dots.split('\n')
        int_dots_list = list(map(lambda s: [int(x) for x in s.split(',')], dots_list))

        folds_list = folds.split('\n')
        extract_folds_list = list(map(lambda s: re.search('[xy]=[0-9]+', s).group(0), folds_list))

        return int_dots_list, extract_folds_list


def folding(coord, fold_line, dots_overlap):
    fold_along = fold_line[0]
    fold_along_index = int(fold_line[fold_line.index('=') + 1:])
    x, y = coord

    if fold_along == 'y':
        if y > fold_along_index:
            y = 2 * fold_along_index - y
        dots_overlap.add((x, y))

    elif fold_along == 'x':
        if x > fold_along_index:
            x = 2 * fold_along_index - x
        dots_overlap.add((x, y))

    return dots_overlap


def print_grid(dots):
    grid = [['  '] * 40 for _i in range(6)]
    for dot in dots:
        i, j = dot
        grid[j][i] = 'XX'

    for line in grid:
        print(''.join(line))


def part1(dots_list, folds_list):
    first_fold = folds_list[0]
    dots_overlap = set()
    for dot in dots_list:
        dots_overlap = folding(dot, first_fold, dots_overlap)

    print(len(dots_overlap))


def part2(dots_list, folds_list):
    for fold in folds_list:
        dots_overlap = set()
        for dot in dots_list:
            dots_overlap = folding(dot, fold, dots_overlap)
        dots_list = dots_overlap

    print_grid(dots_list)


if __name__ == '__main__':
    part1(*get_input('day13.txt'))
    part2(*get_input('day13.txt'))
