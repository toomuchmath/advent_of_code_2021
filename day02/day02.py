from functools import reduce


def into_list(filename):
    with open(filename) as f:
        instructions = f.read().split('\n')
        return instructions


def sum_direction(instructions, direction):

    direction_instructions = filter(lambda s: direction in s, instructions)
    direction_steps = map(lambda s: s.split(), direction_instructions)
    direction_sum = sum([int(x) for _, x in direction_steps])

    return direction_sum


def part1(instructions):
    return sum_direction(instructions, 'forward') * \
           (sum_direction(instructions, 'down') - sum_direction(instructions, 'up'))


def part2_reducer(counters, instructions):
    direction, step_str = instructions
    step = int(step_str)
    horizontal, depth, aim = counters

    if direction == 'forward':
        return horizontal + step, depth + (aim * step), aim
    elif direction == 'down':
        return horizontal, depth, aim + step
    else:
        return horizontal, depth, aim - step


def part2(instructions):
    split_instructions = map(lambda s: s.split(), instructions)
    horizontal, depth, _aim = reduce(part2_reducer, split_instructions, (0, 0, 0))
    return horizontal * depth


if __name__ == '__main__':
    print(part1(into_list('day02.txt')))
    print(part2(into_list('day02.txt')))
