class Player:
    def __init__(self):
        self.player_number = None

class Game:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.winner = None

    def test(self):
        players = [self.p1, self.p2] #list of players
        winner = 2 #example - corresponds to player 2
        self.winner = players[winner - 1] #corresponds to player 2
        #PROBLEM - returning object(?) instead of 'player2'

        # OR

#        win = 'player' #initializing the winner variable
#        winner = 2 #example - corresponds to player 2
#        win += str(winner) #makes 2 a string
#        self.winner = win #self.winner = 'player2'
        #PROBLEM - maybe when running the game, the argument would be 'Christine' instead of 'player2'


player1 = Player()
player2 = Player()
game = Game(player1, player2)
game.test()
print(game.winner)