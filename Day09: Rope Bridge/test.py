import unittest

from index import positions_tail_visits_at_least_once, data_string_to_command, Command, Direction, perform_move, Vector


class TestDataStringToCommand(unittest.TestCase):
    def test_data_string_to_command_1(self):
        eg_data_string = "L 19"
        command = data_string_to_command(eg_data_string)
        self.assertEqual(command, Command(direction=Direction.LEFT, magnitude=19))


class TestPerformMove(unittest.TestCase):
    def test_perform_move_1(self):
        cmd = Command(direction=Direction.RIGHT, magnitude=3)
        head = Vector(0, 0)
        tail = Vector(0, 0)
        perform_move(head, tail, cmd)
        self.assertEqual(Vector(3, 0), head)
        self.assertEqual(Vector(2, 0), tail)

    def test_perform_move_2(self):
        # Head moving away from a diagonal
        cmd = Command(direction=Direction.UP, magnitude=1)
        head = Vector(1, 1)
        tail = Vector(0, 0)
        perform_move(head, tail, cmd)
        self.assertEqual(Vector(1, 2), head)
        self.assertEqual(Vector(1, 1), tail)

    def test_perform_move_3(self):
        # Head moving in alignment from a diagonal
        cmd = Command(direction=Direction.DOWN, magnitude=2)
        head = Vector(1, 1)
        tail = Vector(0, 0)
        perform_move(head, tail, cmd)
        self.assertEqual(Vector(1, -1), head)
        self.assertEqual(Vector(0, 0), tail)

    def test_perform_move_4(self):
        cmd1 = Command(direction=Direction.UP, magnitude=1)
        head = Vector(0, 0)
        tail = Vector(0, 0)
        cmd2 = Command(direction=Direction.RIGHT, magnitude=3)
        perform_move(head, tail, cmd1)
        perform_move(head, tail, cmd2)
        self.assertEqual(Vector(3, 1), head)
        self.assertEqual(Vector(2, 1), tail)


class TestPositions(unittest.TestCase):
    def test_positions_tail_visits_at_least_once_1(self):
        commands: list[str] = '''
            L 3
        '''.strip().replace(" ", "").splitlines()
        commands: list[Command] = [data_string_to_command(command) for command in commands]
        positions = positions_tail_visits_at_least_once(commands)
        self.assertEqual(
            sorted(((0, 0), (-1, 0), (-2, 0))),
            sorted(positions)
        )

    def test_positions_tail_visits_at_least_once_2(self):
        commands: list[str] = '''
            U 1
            R 3
        '''.strip().replace(" ", "").splitlines()
        commands: list[Command] = [data_string_to_command(command) for command in commands]
        positions = positions_tail_visits_at_least_once(commands)
        self.assertEqual(
            sorted(((0, 0), (1, 1), (2, 1))),
            sorted(positions)
        )
