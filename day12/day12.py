def get_input(filename):
    with open(filename) as f:
        input_file = f.read().split('\n')
        return input_file


def into_graph(input_file):
    def add_to_graph(p1, p2):
        p1_in_graph = graph.get(p1)
        if p1_in_graph:
            p1_in_graph.add(p2)
        else:
            graph[p1] = {p2}

    graph = dict()
    for line in input_file:
        point1, point2 = line.split('-')
        if point1 == 'start' or point2 == 'end':
            add_to_graph(point1, point2)
        elif point2 == 'start' or point1 == 'end':
            add_to_graph(point2, point1)
        else:
            add_to_graph(point1, point2)
            add_to_graph(point2, point1)

    return graph


def depth_first_search(graph, current_point, visited, path_count):
    visited.append(current_point)

    for next_point in graph[current_point]:
        if next_point == 'end':
            path_count += 1
        elif next_point.isupper() or next_point not in visited:
            path_count = depth_first_search(graph, next_point, visited, path_count)
            visited.remove(next_point)


    return path_count


def dfs_with_condition(graph, current_point, visited, path_count, small_cave_twice):
    if current_point.islower() and current_point in visited:
        small_cave_twice = 1

    visited.append(current_point)

    for next_point in graph[current_point]:
        if next_point == 'end':
            path_count += 1
        elif next_point.isupper() or next_point not in visited or not small_cave_twice:
            path_count = dfs_with_condition(graph, next_point, visited, path_count, small_cave_twice)
            visited.remove(next_point)

    return path_count


def main(input_list):
    graph = into_graph(input_list)

    part1_path_count = depth_first_search(graph, 'start', ['end'], 0)
    print(part1_path_count)

    part2_path_count = dfs_with_condition(graph, 'start', ['end'], 0, 0)
    print(part2_path_count)


if __name__ == '__main__':
    main(get_input('day12.txt'))
