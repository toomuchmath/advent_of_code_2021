from functools import reduce


def get_input_part1(filename):
    with open(filename) as f:
        input_lines = f.read().split('\n')
        output_str = map(lambda s: s.split('| ')[1], input_lines)
        output_list = map(lambda s: s.split(), output_str)

        return output_list


def get_input_part2(filename):
    with open(filename) as f:
        input_lines = f.read().split('\n')
        output_str = map(lambda s: s.split(' | '), input_lines)

        return list(output_str)


def count_unique(current_count, input_list):
    return len(input_list) + current_count


def part1(input_list):
    unique_output = map(lambda l: [s for s in l if len(s) in (2, 3, 4, 7)], input_list)
    unique_count = reduce(count_unique, unique_output, 0)
    print(unique_count)


def alpha_switch(alpha_string):
    switch = [0] * 7
    for alphabet in alpha_string:
        switch[ord(alphabet) - 97] = 1
    return switch


def solve_remaining(given_switches, mapper):
    one = list(filter(lambda x: sum(x) == 2, given_switches))[0]
    four = list(filter(lambda x: sum(x) == 4, given_switches))[0]
    seven = list(filter(lambda x: sum(x) == 3, given_switches))[0]

    seven_diff_one = [seven_i + one_i for seven_i, one_i in zip(seven, one)]
    mapper[seven_diff_one.index(1)] = 0

    for i, switch in enumerate(one):
        if switch:
            if mapper[i] == -1:
                mapper[i] = 2

    for i, switch in enumerate(four):
        if switch:
            if mapper[i] == -1:
                mapper[i] = 3

    unsolved = mapper.index(-1)
    mapper[unsolved] = 6

    return mapper


def solve_map(given_str):

    given_list = given_str.split()
    given_switches = list(map(alpha_switch, given_list))

    sum_switches = reduce(lambda l1, l2: [l1_i + l2_i for l1_i, l2_i in zip(l1, l2)], given_switches)

    mapper = [-1] * 7
    for i, occurrence in enumerate(sum_switches):
        if occurrence == 4:
            mapper[i] = 4
        elif occurrence == 6:
            mapper[i] = 1
        elif occurrence == 9:
            mapper[i] = 5

    solved_mapper = solve_remaining(given_switches, mapper)

    return solved_mapper


def convert_to_digit(output):

    output_length = len(output)
    if output_length == 2:
        return '1'
    elif output_length == 3:
        return '7'
    elif output_length == 4:
        return '4'
    elif output_length == 7:
        return '8'
    else:
        if output_length == 5:
            if sum(output) == 16:
                return '3'
            elif set(output) == {0, 2, 3, 4, 6}:
                return '2'
            elif set(output) == {0, 1, 3, 5, 6}:
                return '5'
            else:
                raise KeyError
        elif output_length == 6:
            if sum(output) == 18:
                return '0'
            elif sum(output) == 19:
                return '6'
            elif sum(output) == 17:
                return '9'
            else:
                raise KeyError
        else:
            raise KeyError


def parse_output(output_str, mapper):

    output_list = output_str.split()
    correct_output = map(lambda s: [mapper[ord(c) - 97] for c in s], output_list)
    digits = ''.join(list(map(convert_to_digit, correct_output)))

    return int(digits)


def part2(input_list):

    def part2_helper(input_line):
        given_str, output_str = input_line
        mapper = solve_map(given_str)
        output = parse_output(output_str, mapper)
        return output

    output_numbers = map(part2_helper, input_list)
    final_sum = reduce(lambda a, b: a + b, output_numbers)

    print(final_sum)


if __name__ == '__main__':
    part1(get_input_part1('day08.txt'))
    part2(get_input_part2('day08.txt'))
