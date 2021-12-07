def get_input(filename):
    with open(filename) as f:
        input_file = f.read().split(',')
        return [int(n) for n in input_file]


def fish_counter(initial_timers, target_day):
    fish_count = [0] * (target_day + 10)
    for timer in initial_timers:
        fish_count[timer] += 1

    for day in range(1, target_day + 1):
        current_count = fish_count[day]
        fish_count[day + 7] += current_count
        fish_count[day + 9] += current_count
        fish_count[day] = 0

    return sum(fish_count)


def improved_fish_counter(initial_timers, target_day):
    fish_count = [0] * 9
    for timer in initial_timers:
        fish_count[timer] += 1

    for day in range(1, target_day + 1):
        current_count = fish_count[day % 9]
        fish_count[(day + 7) % 9] += current_count
        fish_count[day % 9] = current_count

    return sum(fish_count)


if __name__ == '__main__':
    print(fish_counter(get_input('day06.txt'), 80))
    print(fish_counter(get_input('day06.txt'), 256))

    print(improved_fish_counter(get_input('day06.txt'), 80))
    print(improved_fish_counter(get_input('day06.txt'), 256))
