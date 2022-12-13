"""
Coordinate (x, y)
0 y - - > 0
x
|
v
0
"""


class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return f"row={self.row}, col={self.col}"


def get_data():
    with open("input.txt", "r") as outfile:
        grid = outfile.read()
    return grid


def grid_to_row_col_lists(grid: str) -> (list[list[int]], list[list[int]]):
    grid_rows = grid.splitlines()
    grid_columns = list(map(list, zip(*grid_rows)))  # Transpose list of lists

    row_grid_lines = [[int(tree_height) for tree_height in list(row)] for row in grid_rows]
    col_grid_lines = [[int(tree_height) for tree_height in list(col)] for col in grid_columns]

    return row_grid_lines, col_grid_lines


def get_visible_tree_indexes_for_line(tree_line: list[int]) -> set[int]:
    visible_tree_indexes = set()

    range_left_right = range(0, len(tree_line))
    range_right_left = range(len(tree_line) - 1, 0, -1)

    for my_range in [range_left_right, range_right_left]:
        current_height = -1
        for index in my_range:
            tree_height = tree_line[index]
            if tree_height > current_height:
                visible_tree_indexes.add(index)
                current_height = tree_height

    return visible_tree_indexes


def get_visible_tree_coordinates_for_rows_cols(row_list: list[list[int]], col_list: list[list[int]]) -> set[tuple[int, int]]:
    visible_tree_coords: set[tuple] = set()
    for x, row in enumerate(row_list):
        y_values: set[int] = get_visible_tree_indexes_for_line(row)
        for y in y_values:
            visible_tree_coords.add((x, y))
    for y, col in enumerate(col_list):
        x_values: set[int] = get_visible_tree_indexes_for_line(col)
        for x in x_values:
            visible_tree_coords.add((x, y))

    return visible_tree_coords


def get_viewing_distances_for_tree_in_line(tree_index: int, line: list[int]) -> tuple[int, int]:
    main_tree_height = line[tree_index]
    viewing_distance_left = 0
    trees_to_left = line[0:tree_index]
    trees_to_right = line[tree_index + 1:]
    for tree_height in reversed(trees_to_left):
        if len(trees_to_left) == 0:
            viewing_distance_left = 1
            break
        viewing_distance_left += 1
        if tree_height >= main_tree_height:
            break

    viewing_distance_right = 0
    for tree_height in trees_to_right:
        if len(trees_to_right) == 0:
            viewing_distance_right = 1
            break
        viewing_distance_right += 1
        if tree_height >= main_tree_height:
            break

    return viewing_distance_left, viewing_distance_right


def get_scenic_score_tree_coordinate(row_list: list[list[int]], col_list: list[list[int]],
                                     coord: Coordinate) -> int:
    row_index: int = coord.row
    col_index: int = coord.col
    target_row = row_list[row_index]
    target_col = col_list[col_index]
    dist_y1, dist_y2 = get_viewing_distances_for_tree_in_line(col_index, target_row)
    dist_x1, dist_x2 = get_viewing_distances_for_tree_in_line(row_index, target_col)

    scenic_score: int = dist_y1 * dist_y2 * dist_x1 * dist_x2
    return scenic_score


def get_scenic_score_tree_coordinate_backup(row_list: list[list[int]], col_list: list[list[int]],
                                     coord: Coordinate) -> int:
    row_index: int = coord.row
    col_index: int = coord.col
    target_row = row_list[row_index]
    target_col = col_list[col_index]
    dist_y1, dist_y2 = get_viewing_distances_for_tree_in_line(col_index, target_row)
    dist_x1, dist_x2 = get_viewing_distances_for_tree_in_line(row_index, target_col)

    scenic_score: int = dist_y1 * dist_y2 * dist_x1 * dist_x2
    return scenic_score


def get_highest_scenic_score_in_forest(row_list: list[list[int]], col_list: list[list[int]]) -> int:
    scenic_scores: tuple[int:tuple[int:int]] = []
    for y, row in enumerate(row_list):
        for x, col in enumerate(col_list):
            scenic_scores.append((get_scenic_score_tree_coordinate(row_list, col_list, Coordinate(row=x, col=y)),
                                  Coordinate(row=x, col=y)))
    scenic_scores_sorted = tuple(sorted(scenic_scores, key=lambda item: item[0]))
    highest_score = scenic_scores_sorted[-1][0]
    return highest_score


if __name__ == "__main__":
    grid_data = get_data()
    rows, cols = grid_to_row_col_lists(grid_data)
    visible_tree_coordinates = get_visible_tree_coordinates_for_rows_cols(rows, cols)
    # Part 1
    print(f"Visible Tree Count: {len(visible_tree_coordinates)}")
    # Part 2
    highest_scenic_score = get_highest_scenic_score_in_forest(rows, cols)
    print(f"Highest Scenic Score: {highest_scenic_score}")
