def _route_exists(from_row, from_column, to_row, to_column, map_matrix,visited,n_row,n_col):
    if from_row < 0 or from_row>=n_row or from_column<0 or from_column>=n_col:
        return False

    # valid index from now
    val = map_matrix[from_row][from_column]
    if from_row==to_row and from_column==to_column:
        return val
    elif not val or visited[from_row][from_column]:
        return False

    visited[from_row][from_column] = True
    return (
        _route_exists(from_row-1,from_column,to_row,to_column,map_matrix,visited,n_row,n_col)
        or _route_exists(from_row+1,from_column,to_row,to_column,map_matrix,visited,n_row,n_col)
        or _route_exists(from_row,from_column-1,to_row,to_column,map_matrix,visited,n_row,n_col)
        or _route_exists(from_row,from_column+1,to_row,to_column,map_matrix,visited,n_row,n_col)
    )

def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    n_row = len(map_matrix)
    n_col = len(map_matrix[0])
    visited = [[False for _ in range(n_col)] for _ in range(n_row)]
    return _route_exists(from_row,from_column,to_row,to_column,map_matrix,visited,n_row,n_col)

if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];
    print(route_exists(0, 0, 2, 2, map_matrix))