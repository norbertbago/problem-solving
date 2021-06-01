def get_row_col(string):
    board = ["A", "B", "C"]
    column = board.index(string[0])
    row = int(string[1])
    d = (row-1, column)
    return d

get_row_col("A3")