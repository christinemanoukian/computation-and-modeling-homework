import random
import numpy as np

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
        win = 'player' #initializing the winner variable
        open_spaces = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    open_spaces.append((i,j))
        if open_spaces == []:
            self.winner = 'tie'
        else:
            if self.board[0][0] == self.board[0][1] == self.board[0][2]:
                win += str(self.board[0][0])
                self.winner = win
            if self.board[1][0] == self.board[1][1] == self.board[1][2]:
                win += str(self.board[1][0])
                self.winner = win
            if self.board[2][0] == self.board[2][1] == self.board[2][2]:
                win += str(self.board[2][0])
                self.winner = win
            if self.board[0][0] == self.board[1][0] == self.board[2][0]:
                win += str(self.board[0][0])
                self.winner = win
            if self.board[0][1] == self.board[1][1] == self.board[2][1]:
                win += str(self.board[0][1])
                self.winner = win
            if self.board[0][2] == self.board[1][2] == self.board[2][2]:
                win += str(self.board[0][2])
                self.winner = win
            if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                win += str(self.board[0][0])
                self.winner = win
            if self.board[0][2] == self.board[1][1] == self.board[2][0]:
                win = self.board[0][2]
                self.winner = win
 
    def run(self):
        while self.winner is None:
            self.move(self.p1)
            self.check_winner()
            if self.winner is not None:
                return self.winner
            else:
                self.move(self.p2)
                self.check_winner()
                if self.winner is not None:
                    return self.winner


player1 = Player()
player2 = Player()
game = Game(player1, player2)
game.run()
print(game.winner)