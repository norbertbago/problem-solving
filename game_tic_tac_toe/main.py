from welcome_window import welcome_window
from game_board import default_game, print_game


rows = 3
colums = 3 

player_1 = "x"
player_2 = "o"


welcome_window()
game = default_game(rows, colums)
print_game(game, rows, colums)


