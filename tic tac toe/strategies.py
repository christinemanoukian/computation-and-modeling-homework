def random_strategy_function(board):
    open_spaces = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                open_spaces.append((i,j))
    else:
        return random.choices(open_spaces)[0]

def custom_strategy_function(board):
    