def default_game(rows, colums):
  game = []
  for i in range(rows):
    game_row = []
    for j in range(colums):
      game_row.append('_')
    game.append(game_row)
  return game

def print_game(game, rows, colums):
    print()
    print(" ", end=" ")
    for row in range(rows):
        print(row, end=" ")
    print()
    for row in range(rows):
        print(row , end=" ")
        for col in range(colums):
            print(game[row][col], end=" ")
        print()
    print()

