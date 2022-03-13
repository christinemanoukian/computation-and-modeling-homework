import random


class Player:
    def __init__(self):
        self.player_number = None

    def choose_move(self, board):
        open_spaces = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    open_spaces.append((i,j))
        else:
            return random.choices(open_spaces)[0]



class Game:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.board = [[0 for j in range(3)] for i in range(3)]
        self.p1.player_number = 1
        self.p2.player_number = 2
        self.winner = None

    def move(self, player):
        i,j = player.choose_move(self.board)
        self.board[i][j] = player.player_number

    def check_winner(self):
        open_spaces = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    open_spaces.append((i,j))
        if open_spaces == []:
            self.winner = 'tie'
        else:
        # go thru instances of a win, if it's a win, do one of the options in test file (not sure which is better or if 
        # there's an option better that I don't know of

 
    def run(self):
        while self.winner == None:
            self.move(self.p1)
            self.check_winner()
            if self.winner != None:
                return self.winner
            else:
                self.move(self.p2)
                self.check_winner()
                if self.winner != None:
                    return self.winner

# ask about log=true
# code tie instance

# turn board into matrix just for fun
            



player1 = Player()
player2 = Player()
game = Game(player1, player2)
print(game.run())