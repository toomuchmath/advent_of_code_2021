def into_list(filename):
    with open(filename) as f:
        numbers = f.read().split('\n')
        numbers = list(map(int, numbers))
        return numbers


def count_increases(input_list, offset):

    diff_list = [a_i - b_i for a_i, b_i in zip(input_list[offset:], input_list[:-offset])]
    total_increases = sum(map(lambda x: x > 0, diff_list))
    return total_increases


if __name__ == '__main__':
    # part 1
    print(count_increases(into_list('day01.txt'), 1))
    # part 2
    print(count_increases(into_list('day01.txt'), 3))

