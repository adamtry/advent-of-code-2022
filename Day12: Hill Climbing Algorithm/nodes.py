class Node:
    def __init__(self, row, col, value, letter):
        self.row: int = row
        self.col: int = col
        self.value: int = value
        self.adjacent_nodes: list[Node] = []
        self.shortest_path: list[Node] = None
        self.letter: str = letter

    def __repr__(self):
        return f"Node(r{self.row}, c{self.col})-[{self.value}|{self.letter}]"

    def __eq__(self, other):
        eq = (self.row, self.col) == (other.row, other.col)
        return eq


class NodePath:
    def __init__(self, nodes):
        self.nodes: list[Node] = nodes

    def length(self):
        return len(self.nodes)

    def last_node(self):
        return self.nodes[-1]

    def move(self):
        new_paths = []
        for adjacent_node in self.last_node().adjacent_nodes:
            if adjacent_node.value > self.last_node().value + 1:
                # Abort if adjacent node too high
                continue
            if adjacent_node.shortest_path is None:
                adjacent_node.shortest_path = self.nodes
            elif self.length() >= len(adjacent_node.shortest_path):
                # Abort if there is a faster or equal path to the node
                continue
            else:
                # Set shortest path with current length
                adjacent_node.shortest_path = self.nodes
            new_path = NodePath(self.nodes + [adjacent_node])
            new_paths.append(new_path)
        return new_paths

    def __repr__(self):
        return f"r{self.last_node().row}, c{self.last_node().col} [{self.length()}]"

    def __eq__(self, other):
        return self.nodes == other.nodes
