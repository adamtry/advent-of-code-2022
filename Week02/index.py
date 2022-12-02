class Move:
    Rock = "R"
    Paper = "P"
    Scissors = "S"

def get_winning_move_for(input_move: str) -> str:
    if input_move == Move.Rock:
        return Move.Paper
    elif input_move == Move.Paper:
        return Move.Scissors
    elif input_move == Move.Scissors:
        return Move.Rock

def get_drawn_move_for(input_move: str) -> str:
    return input_move

def get_losing_move_for(input_move: str) -> str:
    if input_move == Move.Rock:
        return Move.Scissors
    elif input_move == Move.Paper:
        return Move.Rock
    elif input_move == Move.Scissors:
        return Move.Paper

def game_string_to_score(raw_game_string: str, right_for_outcome: bool) -> int:
    outcome_score = 0
    choice_score = 0
    # Standardise string
    _game_string = raw_game_string.replace("A", Move.Rock).replace("B", Move.Paper).replace("C", Move.Scissors)
    opponent_move = _game_string.split()[0]
    for character, replacement in [
            ("X", get_losing_move_for(opponent_move) if right_for_outcome else Move.Rock),
            ("Y", get_drawn_move_for(opponent_move) if right_for_outcome else Move.Paper),
            ("Z", get_winning_move_for(opponent_move) if right_for_outcome else Move.Scissors)]:
        parsed_game_string = _game_string.replace(character, replacement)

    player_move = parsed_game_string.split()[-1]

    # Calculate outcome score
    if player_move == get_winning_move_for(opponent_move):
        outcome_score += 6
    elif player_move == get_drawn_move_for(opponent_move):
        outcome_score += 3

    # Add choice score
    if player_move == Move.Rock:
        choice_score += 1
    elif player_move == Move.Paper:
        choice_score += 2
    elif player_move == Move.Scissors:
        choice_score += 3

    return outcome_score + choice_score


if __name__ == "__main__":
    with open("input.txt", "r") as outfile:
        rps_data = outfile.read()

    for right_is_outcome_part2 in [False, True]:
        score = 0
        for game_string_line in rps_data.splitlines():
            score += game_string_to_score(game_string_line, right_is_outcome_part2)
        print(score)
