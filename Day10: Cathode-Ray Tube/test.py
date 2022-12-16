import unittest
from index import file_to_instructions, Instruction, CRTProgram


class TestFileToInstructions(unittest.TestCase):
    def test_file_to_instructions(self):
        instructions = file_to_instructions(filename="input.txt")

        self.assertEqual(len(instructions), 141)
        self.assertEqual(instructions[131].add_register, -17)


class E2E(unittest.TestCase):

    def test_ss_at_cycle_e2e(self):
        instructions = file_to_instructions("test_input.txt")
        crt = CRTProgram(instructions)

        test_cycle_signal_strength = [
            (1, 1), (2, 2), (20, 420), (60, 1140), (100, 1800), (180, 2880), (220, 3960)
        ]

        for test_item in test_cycle_signal_strength:
            cycle = test_item[0]
            expected_ss = test_item[-1]

            self.assertEqual(
                expected_ss,
                crt.get_signal_strength_at_cycle(cycle)
            )


if __name__ == "__main__":
    unittest.main()
