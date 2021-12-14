def get_input(filename):
    with open(filename) as f:
        input_file = f.read().split(',')
        return [int(n) for n in input_file]