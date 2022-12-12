import unittest
from index import find_packet_indexes, is_marker


class TestIsMarker(unittest.TestCase):

    def test_is_marker(self):
        marker = "spam"
        long_marker = "abcdefghijklmn"
        not_marker = "eggs"
        self.assertTrue(is_marker(marker), marker + " should be marker")
        self.assertTrue(is_marker(long_marker), long_marker + " should be marker")
        self.assertFalse(is_marker(not_marker), marker + " should not be marker")


class TestFindPacketIndexes(unittest.TestCase):

    def test_find_packet_indexes(self):
        self.assertEqual(
            find_packet_indexes("mjqjpqmgbljsphdztnvjfqwrcgsmlb", signal_width=4)[0], 7
        )

    def test_get_first_packet_index_2(self):
        self.assertEqual(
            find_packet_indexes("bvwbjplbgvbhsrlpgdmjqwftvncz", signal_width=4)[0], 5
        )

    def test_get_first_packet_index_3(self):
        self.assertEqual(
            find_packet_indexes("mjqjpqmgbljsphdztnvjfqwrcgsmlb", signal_width=14)[0], 19
        )

    def test_get_first_packet_index_4(self):
        self.assertEqual(
            find_packet_indexes("bvwbjplbgvbhsrlpgdmjqwftvncz", signal_width=14)[0], 23
        )


if __name__ == '__main__':
    unittest.main()
