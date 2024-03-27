def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
    n_row = len(game_matrix)
    n_col = len(game_matrix[0])

    if to_row < 0 or to_row >= n_row or to_column < 0 or to_column >= n_col:
        return False
    
    if from_row != to_row and from_column != to_column:
        return False
    
    if from_row == to_row:
        diff_col = to_column-from_column
        if abs(diff_col) != 1:
            return False
        return game_matrix[from_row][to_column]
    else:
        diff_row = to_row-from_row
        if diff_row==2:
            # right
            return game_matrix[from_row+1][from_column] and game_matrix[from_row+2][from_column]
        elif diff_row == -2:
            return game_matrix[from_row-1][from_column] and game_matrix[from_row-2][from_column]
        else:
            return False


if __name__ == "__main__":
    game_matrix = [
        [False, False, True, True, False],
        [False, False, True, False, False],
        [False, False, True, True, False],
        [False, True, False, True, False],
        [False, False, True, False, False]
    ]

    print(can_travel_to(game_matrix, 2, 2, 0, 2))
    print(can_travel_to(game_matrix, 2, 2, 2, 1))
    print(can_travel_to(game_matrix, 2, 2, 2, 3))
    print(can_travel_to(game_matrix, 2, 2, 4, 2))