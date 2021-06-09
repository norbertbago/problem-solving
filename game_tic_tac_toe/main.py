from welcome_window import welcome_window, start_game
from game_board import default_game, print_game

rows = 3
colums = 3 
game = default_game(rows, colums)
empty_places = rows*colums

#welcome_window()
for round_id in range(1,6):
    print("Round number is ", round_id)
    for player in range(0, 2):
        print_game(game, rows, colums)
        






