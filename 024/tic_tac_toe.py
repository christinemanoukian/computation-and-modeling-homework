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
        self.log = False
    
    def print_board(self):
        print(f'{self.board[0][0]} {self.board[0][1]} {self.board[0][2]}\n{self.board[1][0]} {self.board[1][1]} {self.board[1][2]}\n{self.board[2][0]} {self.board[2][1]} {self.board[2][2]}')

    def move(self, player):
        if self.log:
            print(f'Fetching move from player {player.player_number}')
        i,j = player.choose_move(self.board)
        if self.log:
            print(f'Updating board: player {player.player_number} moves into coordinates {i},{j}')
        self.board[i][j] = player.player_number
        if self.log:
            self.print_board()

    def check_winner(self):
        open_spaces = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    open_spaces.append((i,j))
        if self.log:
            print(f'Checking open spaces: {open_spaces}')
        if open_spaces == []:
            self.winner = 'tie'
        else:
            if self.board[0][0] == self.board[0][1] == self.board[0][2] != 0:
                self.winner = self.board[0][0]
            if self.board[1][0] == self.board[1][1] == self.board[1][2] != 0:
                self.winner = self.board[1][0]
            if self.board[2][0] == self.board[2][1] == self.board[2][2] != 0:
                self.winner = self.board[2][0]
            if self.board[0][0] == self.board[1][0] == self.board[2][0] != 0:
                self.winner = self.board[0][0]
            if self.board[0][1] == self.board[1][1] == self.board[2][1] != 0:
                self.winner = self.board[0][1]
            if self.board[0][2] == self.board[1][2] == self.board[2][2] != 0:
                self.winner = self.board[0][2]
            if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
                self.winner = self.board[0][0]
            if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
                self.winner = self.board[0][2]
 
    def run(self):
        while self.winner is None:
            self.move(self.p1)
            self.check_winner()
            if self.winner is not None:
                return self.winner
            self.move(self.p2)
            self.check_winner()
            if self.winner is not None:
                return self.winner
        return self.winner
