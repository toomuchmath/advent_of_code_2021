def get_input(filename):
    with open(filename) as f:
        polymer_template, insertion_rules = f.read().split('\n\n')
        insertion_rules_dict = dict(s.split(' -> ') for s in insertion_rules.split('\n'))

        return polymer_template, insertion_rules_dict


def increase_dict_count(dict_name, key_name, increment):
    if dict_name.get(key_name):
        dict_name[key_name] += increment
    else:
        dict_name[key_name] = increment

    return dict_name


def to_dict(template):
    pattern_dict = {}
    for i in range(len(template) - 1):
        pattern = template[i:i + 2]
        pattern_dict = increase_dict_count(pattern_dict, pattern, 1)

    return pattern_dict


def initial_element_count(template):
    element_count = {}
    for element in template:
        element_count = increase_dict_count(element_count, element, 1)

    return element_count


def every_step(template_dict, insertion_rules, element_count):
    new_template = {}

    for pattern, count in template_dict.items():
        new_element = insertion_rules[pattern]
        element_count = increase_dict_count(element_count, new_element, count)

        new_patterns = [pattern[0] + new_element, new_element + pattern[1]]
        for new_pattern in new_patterns:
            new_template = increase_dict_count(new_template, new_pattern, count)

    return new_template, element_count


def main(days, polymer_template, insertion_rules):
    element_count = initial_element_count(polymer_template)
    template_dict = to_dict(polymer_template)

    for step in range(days):
        template_dict, element_count = every_step(template_dict, insertion_rules, element_count)

    element_count_sorted = sorted(element_count.values())
    print(element_count_sorted[-1] - element_count_sorted[0])


if __name__ == '__main__':
    main(10, *get_input('day14.txt'))
    main(40, *get_input('day14.txt'))
