import sys
sys.path.append('024')
from game import *
from player import *
from strategies import *
from ben import *
from celeste import *
from elias import *
from jeff import *

wins = {1: 0, 2: 0, 'ties': 0}
for i in range(1000):
    player1 = Player(random_strategy_function)
    player2 = Player(custom_strategy_function)
    game = Game(player1, player2, log=False)
    game.run()

    if type(game.winner) is int:
        wins[game.winner] += 1
    else:
        wins['ties'] += 1
print(wins)