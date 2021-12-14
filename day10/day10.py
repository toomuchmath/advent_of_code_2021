from functools import reduce


def get_input(filename):
    with open(filename) as f:
        input_file = f.read().split('\n')
        return input_file


def parse_string(input_line):
    opens = []
    for char in input_line:
        if char in ('(', '[', '{', '<'):
            opens.append(char)
        elif char == ')':
            if opens[-1] == '(':
                opens.pop()
            else:
                return char
        elif char == ']':
            if opens[-1] == '[':
                opens.pop()
            else:
                return char
        elif char == '}':
            if opens[-1] == '{':
                opens.pop()
            else:
                return char
        elif char == '>':
            if opens[-1] == '<':
                opens.pop()
            else:
                return char

    return ''.join(opens)


def part1(input_list):
    score_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    corrupted = filter(lambda s: len(s) == 1, map(parse_string, input_list))
    corrupted_score = reduce(lambda a, b: a + b, map(lambda c: score_map[c], corrupted))

    return corrupted_score


def part2(input_list):
    score_map = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }

    unfinished = filter(lambda s: len(s) > 1, map(parse_string, input_list))
    unfinished_points = map(lambda s: [score_map[c] for c in s[::-1]], unfinished)
    unfinished_scores = list(map(lambda points: reduce(lambda a, b: 5 * a + b, points), unfinished_points))

    unfinished_scores.sort()

    midpoint = len(unfinished_scores) // 2
    middle_score = unfinished_scores[midpoint]

    return middle_score


if __name__ == '__main__':
    print(part1(get_input('day10.txt')))
    print(part2(get_input('day10.txt')))

