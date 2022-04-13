import sys
sys.path.append('024')
from tic_tac_toe import *

wins = {1: 0, 2: 0, 'ties': 0}
for i in range(100000):
    player1 = Player(custom_strategy_function)
    player2 = Player(random_strategy_function)
    game = Game(player1, player2)
    game.run()
    if type(game.winner) is int:
        wins[game.winner] += 1
    else:
        wins['ties'] += 1
print(wins)