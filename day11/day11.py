def get_input(filename):
    with open(filename) as f:
        input_file = f.read().split('\n')
        input_list = list(map(lambda l: [int(n) for n in l], input_file))
        return input_list


def get_valid_adjacent(coord):
    i, j = coord

    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def within_range(adjacent_coord):
        adjacent_i, adjacent_j = adjacent_coord
        return 0 <= adjacent_i < 10 and 0 <= adjacent_j < 10

    def get_adjacent(offset):
        offset_i, offset_j = offset
        return i + offset_i, j + offset_j

    return list(filter(within_range, map(get_adjacent, offsets)))


def flash_adjacent(octopus, flashes, resets):
    i, j = flashes[0]
    valid_adjacent = get_valid_adjacent((i, j))
    flashes.remove((i, j))

    for adj_i, adj_j in valid_adjacent:
        octopus[adj_i][adj_j] = (octopus[adj_i][adj_j] + 1) % 10
        if octopus[adj_i][adj_j] == 0:
            flashes.append((adj_i, adj_j))
            resets.add((adj_i, adj_j))

    return flashes, resets


def each_step(input_list):
    flashes = []
    resets = set()

    for i, row in enumerate(input_list):
        for j, col in enumerate(row):
            input_list[i][j] = (col + 1) % 10
            if input_list[i][j] == 0:
                flashes.append((i, j))
                resets.add((i, j))

    while len(flashes) > 0:
        flashes, resets = flash_adjacent(input_list, flashes, resets)

    flash_count = len(resets)
    for reset in resets:
        i, j = reset
        input_list[i][j] = 0

    return flash_count


def part1(input_list):
    total_flash_count = 0

    for step in range(100):
        flash_count = each_step(input_list)
        total_flash_count += flash_count

    print(total_flash_count)


def part2(input_list):
    step_count = 0
    flash_count = 0

    while flash_count != 100:
        step_count += 1
        flash_count = each_step(input_list)

    print(step_count)


if __name__ == '__main__':
    part1(get_input('day11.txt'))
    part2(get_input('day11.txt'))
