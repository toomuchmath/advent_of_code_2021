import statistics


def get_input(filename):
    with open(filename) as f:
        input_file = f.read().split(',')
        return [int(n) for n in input_file]


def part1(submarines):
    median_sub = statistics.median(submarines)
    steps = [abs(pos - median_sub) for pos in submarines]
    return sum(steps)


def part2(submarines):
    target_position = int(statistics.mean(submarines))
    distance = [abs(pos - target_position) for pos in submarines]
    steps = [d * (d + 1) / 2 for d in distance]
    return sum(steps)


if __name__ == '__main__':
    print(part1(get_input('day07.txt')))
    print(part2(get_input('day07.txt')))
