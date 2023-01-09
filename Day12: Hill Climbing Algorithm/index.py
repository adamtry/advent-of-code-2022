import string
from image_generator import ImageGenerator
from nodes import Node, NodePath

def get_data(filename):
    with open(filename, "r") as outfile:
        map_lines = outfile.read().splitlines()

    letter_indexes = {}
    for i, letter in enumerate(string.ascii_lowercase):
        letter_indexes[letter] = i + 1

    node_map: dict[tuple:Node] = {}
    start_node, end_node = None, None
    for row, line in enumerate(map_lines):
        for col, character in enumerate(list(line)):
            if character == "S":
                node = Node(row, col, 0, character)
                start_node = node
            elif character == "E":
                node = Node(row, col, 26, character)
                end_node = node
            else:
                letter_index = letter_indexes[character]
                node = Node(row, col, letter_index, character)
            node_map[(row, col)] = node

    node_list: list[Node] = []

    # Flatten the nodes + set adjacent_nodes

    for coordinate, node in node_map.items():
        adjacent_nodes = []
        for direction in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            try:
                adjacent_node = node_map[(coordinate[0] + direction[0], coordinate[1] + direction[1])]
                adjacent_nodes.append(adjacent_node)
            except KeyError:
                continue
        node.adjacent_nodes = adjacent_nodes
        node_list.append(node)
    assert isinstance(start_node, Node) and isinstance(end_node, Node)
    return start_node, end_node, node_list


if __name__ == "__main__":
    start, end, grid = get_data("input.txt")
    image_generator = ImageGenerator(start_node=start, end_node=end, nodes=grid, paths=None)
    node_path = NodePath(nodes=[start])
    paths = node_path.move()
    found = False
    while found == False:
        new_paths = []
        for path in paths:
            new_paths += path.move()
            if end in path.nodes:
                steps = path.length() - 1
                print(f"FOUND in {steps} steps")
                found = True
                break
        if len(new_paths) == 0:
            break
        image_generator.draw_paths(new_paths)
        paths = new_paths

    image_generator.make_gif("path_animation", "maps")

