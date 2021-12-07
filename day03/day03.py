def into_list(filename):
    with open(filename) as f:
        instructions = f.read().split('\n')
        return instructions


def part1(input_list):
    transposed_instructions = map(list, zip(*input_list))
    max_occurrence_binary = ''.join(list(map(lambda l: max(l, key=l.count), transposed_instructions)))

    max_occurrence_decimal = int(max_occurrence_binary, 2)
    min_occurrence_decimal = 2 ** len(max_occurrence_binary) - 1 - max_occurrence_decimal

    return max_occurrence_decimal * min_occurrence_decimal


def part2_helper(rating_list, criteria):

    if criteria == 'most':
        if_most0 = '0'
        if_most1 = '1'
    elif criteria == 'least':
        if_most0 = '1'
        if_most1 = '0'
    else:
        raise ValueError("criteria can only be most or least")

    i = 0
    while len(rating_list) > 1:
        i_digits = [int(x[i]) for x in rating_list]
        count1 = sum(i_digits)
        count0 = len(i_digits) - count1

        if count1 < count0:
            rating_list = [x for x in rating_list if x[i] == if_most0]
        else:
            rating_list = [x for x in rating_list if x[i] == if_most1]

        i += 1

    return rating_list[0]



def part2(input_list):

    oxy_rating = part2_helper(input_list, 'most')
    co2_rating = part2_helper(input_list, 'least')

    return int(oxy_rating, 2) * int(co2_rating, 2)


if __name__ == '__main__':
    print(part1(into_list('day03.txt')))
    print(part2(into_list('day03.txt')))
