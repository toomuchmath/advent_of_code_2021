def get_input(filename):

    def to_int(row):
        start, end = row
        start_x, start_y = [int(p) for p in start.split(',')]
        end_x, end_y = [int(p) for p in end.split(',')]
        return [start_x, start_y, end_x, end_y]

    with open(filename) as f:
        input_file = f.read().split('\n')
        input_split = map(lambda s: s.split(' -> '), input_file)
        input_int = list(map(lambda r: to_int(r), input_split))

        return input_int


def danger_tracker(coord_x, coord_y, danger_points, danger_count):
    if danger_points.get((coord_x, coord_y)):
        danger_points[(coord_x, coord_y)] += 1
        if danger_points.get((coord_x, coord_y)) == 2:
            danger_count += 1

    else:
        danger_points[(coord_x, coord_y)] = 1

    return danger_points, danger_count


def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def walk_danger_points(row, danger_points, danger_count):
    start_x, start_y, end_x, end_y = row
    diff_x, diff_y = end_x - start_x, end_y - start_y
    sign_x, sign_y = sign(diff_x), sign(diff_y)

    for step in range(max(abs(diff_x), abs(diff_y)) + 1):
        step_x, step_y = list(map(lambda n: n * step, [sign_x, sign_y]))
        danger_points, danger_count = danger_tracker(start_x + step_x, start_y + step_y, danger_points, danger_count)

    return danger_points, danger_count


def part1(input_list):
    danger_points = dict()
    danger_count = 0

    for row in input_list:
        start_x, start_y, end_x, end_y = row
        if start_x == end_x or start_y == end_y:
            danger_points, danger_count = walk_danger_points(row, danger_points, danger_count)

    return danger_count


def part2(input_list):
    danger_points = dict()
    danger_count = 0

    for row in input_list:
        danger_points, danger_count = walk_danger_points(row, danger_points, danger_count)

    return danger_count


if __name__ == '__main__':
    print(part1(get_input('day05.txt')))
    print(part2(get_input('day05.txt')))
