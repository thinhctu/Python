import random

def initialize():
#making an empty 4x4 board
    mat =[]
    for i in range(4):
        mat.append([0] * 4)
    print("Welcome to 2048! Control using WASD")
    #add tile
    fillTwoOrFour(mat)
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in mat]))

    #print(mat)
    return mat

def checkGameStatus(board, max_tile=2048):
    flat_board = [cell for row in board for cell in row]
    if max_tile in flat_board:
        # game has been won if max_tile value is found
        return "YOU WIN!"

    for i in range(4):
        for j in range(4):
            # check if a merge is possible
            if j != 3 and board[i][j] == board[i][j+1] or \
                    i != 3 and board[i][j] == board[i + 1][j]:
                return "PLAY"

    if 0 not in flat_board:
        return "LOSE"
    else:
        return "PLAY"

def move(direction, board):
    if direction == "w":
        return moveUp(board)
    if direction == "s":
        return moveDown(board)
    if direction == "a":
        return moveLeft(board)
    if direction == "d":
        return moveRight(board)

#fill board with 2 or 4 randomly
def fillTwoOrFour(board, iter=1):
    for _ in range(iter):
        a = random.randint(0, 3)
        b = random.randint(0, 3)
        while(board[a][b] != 0):
            a = random.randint(0, 3)
            b = random.randint(0, 3)
        if sum([cell for row in board for cell in row]) in (0, 2):
            board[a][b] = 2
        else:
            board[a][b] = random.choice((2, 4))
    return board


def moveLeft(board):
    # initial shift
    shiftLeft(board)
    # merge cells
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
                j = 0
    # final shift
    shiftLeft(board)
    return board

# move and merge tiles upwards
def moveUp(board):
    board = rotateLeft(board)
    board = moveLeft(board)
    board = rotateRight(board)
    return board

#move and merge right
def moveRight(board):
    # initial shift
    shiftRight(board)

    # merge cells
    for i in range(4):
        for j in range(3, 0, -1):
            if board[i][j] == board[i][j - 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j - 1] = 0
                j = 0
    # final shift
    shiftRight(board)
    return board

#move and merge down
def moveDown(board):
    board = rotateLeft(board)
    board = moveLeft(board)
    shiftRight(board)
    board = rotateRight(board)
    return board

#shift tiles left
def shiftLeft(board):
    # remove 0's in between numbers
    for i in range(4):
        nums, count = [], 0
        for j in range(4):
            if board[i][j] != 0:
                nums.append(board[i][j])
                count += 1
        board[i] = nums
        board[i].extend([0] * (4 - count))

#shift tiles right
def shiftRight(board):
    # remove 0's in between numbers
    for i in range(4):
        nums, count = [], 0
        for j in range(4):
            if board[i][j] != 0:
                nums.append(board[i][j])
                count += 1
        board[i] = [0] * (4 - count)
        board[i].extend(nums)

#rotating matrix left
def rotateLeft(board):
    b = [[board[j][i] for j in range(4)] for i in range(3, -1, -1)]
    return b

#rotating matrix right
def rotateRight(board):
    b = rotateLeft(board)
    b = rotateLeft(b)
    return rotateLeft(b)