class Instruction:
    def __init__(self, cycles, add_register=0):
        self.cycles: int = cycles
        self.add_register: int = add_register


class CycleLog:
    def __init__(self, cycle_index: int, register: int, signal_strength: int):
        self.cycle_index = cycle_index
        self.register = register
        self.signal_strength = signal_strength

    def __repr__(self):
        return f"{self.cycle_index} cyc * {self.register} x_reg = {self.signal_strength} ss"


class CRTProgram:
    def __init__(self, instructions: list[Instruction]):
        self.instructions: list[Instruction] = instructions
        self.cycle_log: dict[int: CycleLog] = {}
        self._set_signal_strengths_for_cycles()

    def get_signal_strength_at_cycle(self, cycle: int) -> int:
        log_at_index: CycleLog = self.cycle_log[cycle]
        return log_at_index.signal_strength

    def get_sum_of_signal_strengths_at_cycle_indexes(self, cycle_indexes: list[int]) -> int:
        sum_ss = 0
        for cycle_index in cycle_indexes:
            sig_str = self.get_signal_strength_at_cycle(cycle_index)
            sum_ss += sig_str
        return sum_ss

    def _set_signal_strengths_for_cycles(self):
        cycle = 1
        register = 1

        for instruction in self.instructions:
            if instruction.cycles == 1:
                self.cycle_log[cycle] = CycleLog(cycle_index=cycle, register=register, signal_strength=cycle * register)
                cycle += 1

            elif instruction.cycles == 2:
                self.cycle_log[cycle] = CycleLog(cycle_index=cycle, register=register, signal_strength=cycle * register)
                cycle += 1
                self.cycle_log[cycle] = CycleLog(cycle_index=cycle, register=register, signal_strength=cycle * register)
                register += instruction.add_register
                cycle += 1


class CRTScreen:
    def __init__(self, pixels_x: int, pixels_y: int):
        self.pixels_x: int = pixels_x
        self.pixels_y: int = pixels_y
        self.screen = [["." for _ in range(0, self.pixels_x)] for _ in range(0, self.pixels_y)]


def file_to_instructions(filename: str) -> list[Instruction]:
    with open(filename, "r") as outfile:
        raw_instructions: list[str] = outfile.read().splitlines()

    parsed_instructions: list[Instruction] = []

    for instruction in raw_instructions:
        if instruction == "noop":
            parsed_instructions.append(
                Instruction(cycles=1, add_register=0)
            )
        elif instruction.startswith("addx"):
            value = int(instruction[5:])
            parsed_instructions.append(
                Instruction(cycles=2, add_register=value)
            )

    return parsed_instructions


if __name__ == "__main__":
    ins = file_to_instructions("input.txt")
    mr_braun = CRTProgram(ins)

    # Part 1
    test_indexes_p1 = [20, 60, 100, 140, 180, 220]
    sum_ss_p1 = mr_braun.get_sum_of_signal_strengths_at_cycle_indexes(test_indexes_p1)
    assert sum_ss_p1 == 14540

    # TODO: Part 2
