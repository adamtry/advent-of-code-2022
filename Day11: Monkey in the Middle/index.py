import re


class Item:
    def __init__(self, worry_level: int):
        self.worry_level: int = worry_level
        self._initial_worry: int = worry_level

    def __repr__(self):
        if self.worry_level != self._initial_worry:
            return f"Item({self.worry_level} <- {self._initial_worry})"
        else:
            return f"Item({self.worry_level})"

    def __eq__(self, other):
        return self.worry_level == other.worry_level


class Test:
    def __init__(self, test_div_by: int, true_throw_to: int, false_throw_to: int):
        self.test_div_by = test_div_by
        self.true_throw_to = true_throw_to
        self.false_throw_to = false_throw_to

    def __repr__(self):
        return f"Test({self.true_throw_to} if % by {self.test_div_by} else {self.false_throw_to})"

    def monkey_index_to_throw_to(self, item: Item) -> int:
        if item.worry_level % self.test_div_by == 0:
            return self.true_throw_to
        else:
            return self.false_throw_to


class Operation:
    def __init__(self, operation_string: str):
        self.operation_string: str = operation_string

    def __repr__(self):
        return f"Operation({self.operation_string})"

    def execute(self, item: Item):
        if self.operation_string == "old * old":
            return
        operation_string = self.operation_string.replace("old", str(item.worry_level))
        item.worry_level = eval(operation_string)


class Monkey:
    def __init__(self, monkey_index: int, starting_items: list[Item], operation: Operation, test: Test):
        """
        :param starting_items: list of worry levels for items held
        :param operation: formula to determine how worry level changes when item is inspected
        :param test: includes a check for item worry levels, and performs actions based on if check passes
        """
        self.index = monkey_index
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.inspection_count: int = 0

    @classmethod
    def from_monkey_string(cls, monkey_string: str):
        monkey_index: int = int(re.search("Monkey ([0-9]*):", monkey_string).group(1))
        starting_items: list[Item] = [
            Item(int(item)) for item in re.search("Starting items: ([0-9].*)", monkey_string).group(1).split(", ")
        ]
        operation: Operation = Operation(re.search("Operation: new = (.*)", monkey_string).group(1))
        test_divisible_by = int(re.search("Test: divisible by (.*)", monkey_string).group(1))
        test_if_true = int(re.search("If true: throw to monkey (.*)", monkey_string).group(1))
        test_if_false = int(re.search("If false: throw to monkey (.*)", monkey_string).group(1))
        test: Test = Test(test_divisible_by, test_if_true, test_if_false)
        return cls(monkey_index, starting_items, operation, test)

    def __repr__(self):
        return f"Monkey({self.index})"

    def inspect_items(self, monkeys: list):
        for item in self.items:
            self.operation.execute(item)
            item.worry_level = round(item.worry_level // 3)
            throw_to_index: int = self.test.monkey_index_to_throw_to(item)
            for monkey in monkeys:
                if throw_to_index == monkey.index:
                    monkey.items.append(item)
            self.inspection_count += 1
        self.items = []


def _file_to_monkeys(filename: str) -> list[Monkey]:
    with open(filename, "r") as outfile:
        data: str = outfile.read()
    monkey_strings = data.split("\n\n")

    monkeys: list[Monkey] = []

    for monkey_string in monkey_strings:
        monkey = Monkey.from_monkey_string(monkey_string)
        monkeys.append(monkey)

    return monkeys


class Program:
    def __init__(self, filename):
        self.monkeys = _file_to_monkeys(filename)

    def inspection_round(self):
        for monkey in self.monkeys:
            monkey.inspect_items(self.monkeys)

    def monkey_business_after_n_rounds(self, round_count: int) -> int:
        for i in range(0, round_count):
            self.inspection_round()
        inspection_counts: list[int] = []
        for monkey in self.monkeys:
            inspection_counts.append(monkey.inspection_count)
        business = sorted(inspection_counts)[-2] * sorted(inspection_counts)[-1]
        return business


if __name__ == "__main__":
    program = Program("input.txt")
    monkey_business = program.monkey_business_after_n_rounds(20)
    print(monkey_business)

    # 91486 - Too Low
