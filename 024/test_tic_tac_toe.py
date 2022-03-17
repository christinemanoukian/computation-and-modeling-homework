import sys
sys.path.append('024')
from tic_tac_toe import *

wins = {1: 0, 2: 0, 'ties': 0}
for i in range(101):
    player1 = Player()
    player2 = Player()
    game = Game(player1, player2)
    game.run()
    if game.winner == 'Tie':
        wins['ties'] += 1
    if game.winner == player1:
        wins[1] += 1
    if game.winner == player2:
        wins[2] += 1
print(wins)