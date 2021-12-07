def get_inputs(filename):
    with open(filename) as f:
        input_file = f.read().split('\n\n')
        instructions, *puzzles = input_file
        return instructions, puzzles


def puzzle_mapper(puzzle_string):
    split_puzzle_string = map(lambda s: s.split(), puzzle_string)
    puzzle_int = list(map(lambda l: [int(x) for x in l], split_puzzle_string))
    coord_dict = get_coordinates(puzzle_int)

    return coord_dict


def get_coordinates(puzzle):
    coord_dict = dict()
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            coord_dict[puzzle[i][j]] = (i, j)
    return coord_dict


def generate_numbers(number_str):
    for i, n in enumerate(number_str.split(',')):
        yield i, int(n)


def bingo_counter_handler(bingo_counter, index, number):
    if bingo_counter[index]:
        bingo_counter[index].append(number)
    else:
        bingo_counter[index] = [number]


def play_bingo(instructions, bingo_coord):
    calling_numbers = generate_numbers(instructions)
    bingo_row_counter = [None] * 5
    bingo_col_counter = [None] * 5

    for nth, number in calling_numbers:

        if bingo_coord.get(number):
            i, j = bingo_coord.get(number)
            bingo_counter_handler(bingo_row_counter, i, number)
            bingo_counter_handler(bingo_col_counter, j, number)
            bingo_coord.pop(number)

            bingo_condition = (len(bingo_row_counter[i]) == 5) or (len(bingo_col_counter[j]) == 5)
            if bingo_condition:
                return nth, number * sum(bingo_coord.keys())


def main(outcome_func):
    instructions, puzzle = get_inputs('day04.txt')
    puzzle_coord_list = map(puzzle_mapper, map(lambda s: s.split('\n'), puzzle))
    bingo_outcome = map(lambda p: play_bingo(instructions, p), puzzle_coord_list)
    chosen_puzzle_outcome = outcome_func(bingo_outcome, key=lambda t: t[0])

    return chosen_puzzle_outcome


if __name__ == '__main__':
    # part 1: min moves to win
    print(main(min))

    # part 2: max moves to win
    print(main(max))
