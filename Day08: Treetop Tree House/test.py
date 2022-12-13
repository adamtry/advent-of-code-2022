import unittest
from index import get_visible_tree_indexes_for_line, grid_to_row_col_lists, get_visible_tree_coordinates_for_rows_cols, \
    get_viewing_distances_for_tree_in_line, get_scenic_score_tree_coordinate, get_highest_scenic_score_in_forest, \
    Coordinate


class TestTreeStuff(unittest.TestCase):

    def test_get_visible_trees_for_line(self):
        eg_tree_line = [1, 2, 5, 3, 5, 1]
        visible_tree_indexes = get_visible_tree_indexes_for_line(eg_tree_line)
        self.assertEqual({0, 1, 2, 4, 5}, visible_tree_indexes)

        eg_tree_line_2 = [1, 9, 5, 3, 8, 9]
        visible_tree_indexes = get_visible_tree_indexes_for_line(eg_tree_line_2)
        self.assertEqual({0, 1, 5}, visible_tree_indexes)

        eg_tree_line_3 = [1, 1, 1, 1, 1, 1]
        visible_tree_indexes = get_visible_tree_indexes_for_line(eg_tree_line_3)
        self.assertEqual({0, 5}, visible_tree_indexes)

    def test_grid_to_col_row_lists(self):
        eg_grid = '''
            3 0 3 7 3
            2 5 5 1 2
            6 5 3 3 2
            3 3 5 4 9
            3 5 3 9 0
        '''.strip().replace(" ", "")
        # self.assertEqual(eg_grid, "30373\n25512\n65332\n33549\n35390")

        row_list, col_list = grid_to_row_col_lists(eg_grid)
        self.assertEqual(row_list[0], [3, 0, 3, 7, 3])
        self.assertEqual(row_list[-1], [3, 5, 3, 9, 0])
        self.assertEqual(col_list[0], [3, 2, 6, 3, 3])
        self.assertEqual(col_list[-1], [3, 2, 2, 9, 0])

    def test_get_visible_tree_coordinates_for_grid(self):
        eg_grid = '''
            6 5 3 3
            3 3 5 4
            3 5 0 9
            1 1 1 1
        '''.strip().replace(" ", "")

        row_list, col_list = grid_to_row_col_lists(eg_grid)

        visible_coordinates = get_visible_tree_coordinates_for_rows_cols(row_list, col_list)
        self.assertEqual(
            visible_coordinates,
            {(0, 0), (1, 0), (2, 0), (3, 0),
             (0, 1), (2, 1), (3, 1),
             (0, 2), (1, 2), (3, 2),
             (0, 3), (1, 3), (2, 3), (3, 3)}
        )


class TestGetViewingDistances(unittest.TestCase):
    def test_case_1(self):
        eg_tree_index = 2
        eg_line = [3, 0, 3, 7, 3]
        distances = get_viewing_distances_for_tree_in_line(eg_tree_index, eg_line)

        self.assertEqual(
            sorted((2, 1)),
            sorted(distances)
        )

    def test_case_2(self):
        eg_tree_index = 2
        eg_line = [3, 0, 5, 5, 2]
        distances = get_viewing_distances_for_tree_in_line(eg_tree_index, eg_line)

        self.assertEqual(
            sorted((2, 1)),
            sorted(distances)
        )

    def test_case_3(self):
        eg_tree_index = 2
        eg_line = [2, 5, 5, 1, 2]
        distances = get_viewing_distances_for_tree_in_line(eg_tree_index, eg_line)

        self.assertEqual(
            sorted((1, 2)),
            sorted(distances)
        )

    def test_case_5(self):
        eg_tree_index = 1
        eg_line = [2, 5, 5, 1, 2]
        distances = get_viewing_distances_for_tree_in_line(eg_tree_index, eg_line)

        self.assertEqual(
            sorted((1, 1)),
            sorted(distances)
        )

    def test_case_6(self):
        eg_tree_index = 2
        eg_line = [2, 5, 5, 1, 2]
        distances = get_viewing_distances_for_tree_in_line(eg_tree_index, eg_line)

        self.assertEqual(
            sorted((1, 2)),
            sorted(distances)
        )


class OtherTreeTests(unittest.TestCase):
    def test_get_scenic_score_tree_coordinate(self):
        eg_grid = '''
        3 0 3 7 3
        2 5 5 1 2
        6 5 3 3 2
        3 3 5 4 9
        3 5 3 9 0
        '''.strip().replace(" ", "")
        row_list, col_list = grid_to_row_col_lists(eg_grid)
        coordinate = Coordinate(row=1, col=2)
        scenic_score = get_scenic_score_tree_coordinate(row_list, col_list, coordinate)
        self.assertEqual(4, scenic_score)

    def test_get_scenic_score_tree_coordinate_2(self):
        eg_grid = '''
        3 0 3 7 3
        2 5 5 1 2
        6 5 3 3 2
        3 3 5 4 9
        3 5 3 9 0
        '''.strip().replace(" ", "")
        row_list, col_list = grid_to_row_col_lists(eg_grid)
        coordinate = Coordinate(row=0, col=2)
        scenic_score = get_scenic_score_tree_coordinate(row_list, col_list, coordinate)
        self.assertEqual(0, scenic_score)

    def test_get_scenic_score_tree_coordinate_3(self):
        eg_grid = '''
        3 0 3 7 3
        2 5 5 1 2
        6 5 3 3 2
        3 3 5 4 9
        3 5 3 9 0
        '''.strip().replace(" ", "")
        row_list, col_list = grid_to_row_col_lists(eg_grid)
        coordinate = Coordinate(row=3, col=2)
        scenic_score = get_scenic_score_tree_coordinate(row_list, col_list, coordinate)
        self.assertEqual(8, scenic_score)

    def test_get_highest_scenic_score_in_forest(self):
        eg_grid = '''
        3 0 3 7 3
        2 5 5 1 2
        6 5 3 3 2
        3 3 5 4 9
        3 5 3 9 0
        '''.strip().replace(" ", "")
        row_list, col_list = grid_to_row_col_lists(eg_grid)
        scenic_response = get_highest_scenic_score_in_forest(row_list, col_list)
        highest_scenic_score = scenic_response[0]
        self.assertEqual(8, highest_scenic_score)  # r3, c2


if __name__ == '__main__':
    unittest.main()
