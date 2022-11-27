import random

def initiate():
    board = []
    #make a 4x4 board
    for i in range(4):
        board.append([0] * 4)
    print("Control using WASD ")
    add_piece(board)
    return board

def add_piece(board):
# spawn a tile at a random location in the board
    row = random.randint(0,3)
#make sure location is empty
    while(board[row] != 0):
        row = random.randint(0,3)
        col = random.randint(0,3)
    board[row] = 2

def check_game(board):
    for i in range(4):
        for j in range(4):
            if(board[i][j] >= 2048):
                return 'WIN'
#Continue Conditions
#if empty square exists
    for i in range(4):
        for j in range(4):
            if(board[i][j] == 0):
                return 'CONTINUE'
#if space clears up after a move    
    for i in range(3):
        for j in range(3):
            if(board[i][j]== board[i][j + 1] or board[i][j]== board[i + 1][j]):
                return 'CONTINUE'
 
    for i in range(3):
        if(board[i][3]== board[i + 1][3]):
            return 'CONTINUE'

    for j in range(3):
        if(board[3][j]== board[3][j + 1]):
            return 'CONTINUE'

    return 'LOST'