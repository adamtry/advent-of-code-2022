class Direction:
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


class Command:
    def __init__(self, direction: Direction, magnitude: int):
        self.direction: Direction = direction
        self.magnitude: int = magnitude

    def to_unit_vectors(self):
        return [Command(self.direction, 1) for _ in range(0, self.magnitude)]

    def __eq__(self, other):
        if isinstance(other, Command):
            equal_command = (self.direction == other.direction and self.magnitude == other.magnitude)
            return equal_command
        else:
            return False

    def __repr__(self):
        return f"Command({self.direction}, {self.magnitude})"


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def apply_command(self, command: Command):
        if command.direction == Direction.UP:
            self.y += command.magnitude
        elif command.direction == Direction.DOWN:
            self.y -= command.magnitude
        elif command.direction == Direction.RIGHT:
            self.x += command.magnitude
        elif command.direction == Direction.LEFT:
            self.x -= command.magnitude

    def clone(self):
        return Vector(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Vector):
            equal_coordinate = (self.x == other.x and self.y == other.y)
            return equal_coordinate
        else:
            return False

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __hash__(self):
        return hash(str(self))


class SnakeSegment:
    def __init__(self, x: int, y: int, parent_segment=None, child_segment=None):
        self.position: Vector = Vector(x, y)
        self.parent_segment: SnakeSegment = parent_segment
        self.child_segment: SnakeSegment = child_segment
        self.visited_coordinates = {Vector(0, 0)}

    def perform_move(self, command: Command):

        unit_commands = command.to_unit_vectors()
        for unit_command in unit_commands:
            self.position.apply_command(command)
    # Can determine where the next segment moves based on how previous segment moves
    # Need to pass information about prev segment to next segment


def perform_move(head_coord: Vector, tail_coord: Vector, command: Command) -> set[Vector]:
    coords_visited: set[Vector] = set()
    unit_commands = command.to_unit_vectors()
    for unit_command in unit_commands:
        previous_head_coord = head_coord.clone()
        head_coord.apply_command(unit_command)

        coords_diagonal = head_coord.x != tail_coord.x and head_coord.y != tail_coord.y
        double_gap_x = abs(head_coord.x - tail_coord.x) == 2
        double_gap_y = abs(head_coord.y - tail_coord.y) == 2
        moving_adjacent = not double_gap_x and not double_gap_y
        moving_diagonal = coords_diagonal and (double_gap_y or double_gap_x)

        if not moving_adjacent:
            if coords_diagonal and moving_diagonal:
                tail_coord.x = previous_head_coord.x
                tail_coord.y = previous_head_coord.y
            elif head_coord != tail_coord:
                tail_coord.apply_command(unit_command)
            coords_visited.add(tail_coord.clone())
    return coords_visited



def get_data():
    with open("input.txt", "r") as outfile:
        data = outfile.read()
    commands = data.strip().replace(" ", "").splitlines()
    return commands


def data_string_to_command(command_string: str) -> Command:
    direct = command_string[0]
    command = Command(
        direction=direct,
        magnitude=int(command_string[1:])
    )
    return command


'''
Need to check (for 2 coordinates):
    If the x and y coordinates are different (i.e. on a diagonal):
        If the x or y coordinates differ by 2 following the head move:
            Set the tail vector's other coordinate to be the same as the head's
e.g
    . . . .        . . H .
    . . H .  = >>  . . T .
    . T . .        . . . .
'''


def positions_tail_visits_at_least_once(commands: list[Command]) -> int:
    # Why oh why can't stuff just be immutable? T_T
    coordinates_visited: set[tuple[int, int]] = set()
    head_vector = Vector(0, 0)
    tail_vector = Vector(0, 0)
    coordinates_visited.add((tail_vector.x, tail_vector.y))
    for command in commands:
        coords_in_move: set[Vector] = perform_move(head_vector, tail_vector, command)
        for item in list(coords_in_move):
            coordinates_visited.add((item.x, item.y))
    return coordinates_visited


if __name__ == "__main__":
    raw_data = get_data()
    set_commands = []
    for cmd_line in raw_data:
        cmd = data_string_to_command(cmd_line)
        set_commands.append(cmd)
    # Part 1
    positions = positions_tail_visits_at_least_once(set_commands)
    print(len(positions))

    # Part 2
    print("no")

