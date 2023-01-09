import unittest
from index import _file_to_monkeys, Monkey, Item, Test, Operation, Program


class TestFileToMonkeys(unittest.TestCase):
    def test_file_to_monkeys(self):
        monkeys = _file_to_monkeys("test_input.txt")
        self.assertEqual(
            4, len(monkeys)
        )
        self.assertEqual(
            0, monkeys[0].index
        )
        self.assertEqual(
            2, len(monkeys[0].items)
        )
        self.assertEqual(
            "old * 19", monkeys[0].operation.operation_string
        )
        self.assertEqual(
            (23, 2, 3),
            (monkeys[0].test.test_div_by,
             monkeys[0].test.true_throw_to,
             monkeys[0].test.false_throw_to)
        )


class TestMonkey(unittest.TestCase):
    def test_inspect_items(self):
        monkeys = _file_to_monkeys("test_input.txt")

        monkeys[0].inspect_items(monkeys)

        self.assertEqual(
            [],
            monkeys[0].items
        )
        self.assertIn(
            Item(500),
            monkeys[3].items
        )

        monkeys[1].inspect_items(monkeys)

        for item_worry in [20, 23, 27, 26]:
            self.assertIn(
                Item(item_worry),
                monkeys[0].items
            )

    def test_inspection_count(self):
        monkeys = _file_to_monkeys("test_input.txt")
        monkeys[0].inspect_items(monkeys)

        self.assertEqual(
            2,
            monkeys[0].inspection_count
        )


class TestProgram(unittest.TestCase):
    def test_main_1_round(self):
        program = Program(filename="test_input.txt")
        monkey_business = program.monkey_business_after_n_rounds(1)
        self.assertEqual(
            20,
            monkey_business,
        )

    def test_main_20_rounds(self):
        program = Program(filename="test_input.txt")
        monkey_business = program.monkey_business_after_n_rounds(20)
        self.assertEqual(
            101,
            next(monkey for monkey in program.monkeys if monkey.index == 0).inspection_count
        )
        self.assertEqual(
            10605,
            monkey_business,
        )


if __name__ == "__main__":
    unittest.main()
