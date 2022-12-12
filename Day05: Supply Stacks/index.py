import copy
import re

class CraneInstruction:
    from_index: int
    to_index: int

    def __init__(self, amount: int, col_from: int, col_to: int):
        self.amount = amount
        self.col_from = col_from
        self.col_to = col_to

        self.from_index = col_from - 1
        self.to_index = col_to - 1

def preprocess_crate_columns_and_instructions():

    with open("./input.txt", "r") as outfile:
        _raw_lines = outfile.read().splitlines()

    all_line_items = []

    for _line in _raw_lines[0:8]:
        line_items = [_line[k] for k in range(1, 35, 4)]
        all_line_items.append(line_items)

    _crate_columns: list[list[str]] = []
    for i in range(1, 35, 4):
        _crate_columns.append([])

    for col_index in range(0, 9):
        for row_index in range(0, len(all_line_items)):
            if all_line_items[row_index][col_index] not in ["", " "]:
                _crate_columns[col_index].append(all_line_items[row_index][col_index])

    return _raw_lines, _crate_columns


def move_items_in_columns(col_data: list[list[str]], instruction:CraneInstruction, crate_mover_9001=False):

    if not crate_mover_9001: # Part 1
        for _ in range(0, instruction.amount):
            col_data[instruction.to_index].insert(0, col_data[instruction.from_index][0])
            col_data[instruction.from_index].pop(0)

    else: # Part 2
        boxes_to_transfer = col_data[instruction.from_index][0:instruction.amount]
        col_data[instruction.to_index] = boxes_to_transfer + col_data[instruction.to_index] # Add to start of new
        col_data[instruction.from_index] = col_data[instruction.from_index][instruction.amount:] # Remove from old

    return col_data

def parse_instruction(instruction_line:str) -> CraneInstruction:
    instruction_line = instruction_line.strip()
    pattern = 'move ([0-9]+) from ([0-9]) to ([0-9])'
    search = re.search(pattern, instruction_line)
    parsed = CraneInstruction(
        amount=int(search.group(1)),
        col_from=int(search.group(2)),
        col_to=int(search.group(3))
    )
    return parsed

def main(_raw_lines, _crate_columns, crate_mover_9001):
    for line in _raw_lines[10:]:
        _inst = parse_instruction(line)
        _crate_columns = move_items_in_columns(_crate_columns, _inst, crate_mover_9001)
    return "".join([col[0] for col in _crate_columns])

if __name__ == "__main__":
    raw_lines, crate_columns = preprocess_crate_columns_and_instructions()
    crate_columns_2 = copy.deepcopy(crate_columns) # Pointers are scary!
    part_1 = main(raw_lines, crate_columns, crate_mover_9001=False)
    part_2 = main(raw_lines, crate_columns_2, crate_mover_9001=True)
    print(f"Part 1: {part_1}\nPart 2: {part_2})")
