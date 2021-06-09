import numpy as np

ROWS = 6
COLUMNS = 7


def create_board():
    board = np.zeros((ROWS, COLUMNS))
    return board


# flip board
def print_board(board):
    print(np.flip(board, 0))


def is_movement_valid(board, column):
    return board[5][column] == 0


def next_empty_row(board, column):
    for r in range(ROWS):
        if board[r][column] == 0:
            return r


def complete_move(board, row, column, player):
    board[row][column] = player


def check_for_win(board, player):
    for c in range(COLUMNS):
        for r in range(ROWS-3):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c]:
                return True

    for r in range(ROWS):
        for c in range(COLUMNS-3):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3]:
                return True

    for r in range(ROWS-3):
        for c in range(COLUMNS-3):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3]:
                return True

    for r in range(3,ROWS):
        for c in range(COLUMNS-3):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3]:
                return True

    pass


board = create_board()
print_board(board)
game_is_on = True
turn = 0  # even for 1st player and odd for 2nd player
while game_is_on:
    # 1st player
    if turn % 2 == 0:
        column = int(input("1st player makes their move: "))
        if is_movement_valid(board, column):
            row = next_empty_row(board, column)
            complete_move(board, row, column, 1)
            if check_for_win(board, 1):
                print("PLAYER 1!")
                game_is_on = False

    # 2nd player
    else:
        column = int(input("2nd player make their move: "))
        if is_movement_valid(board, column):
            row = next_empty_row(board, column)
            complete_move(board, row, column, 2)
            if check_for_win(board, 2):
                print("PLAYER 2!")
                game_is_on = False

    print_board(board)
    turn += 1
    turn %= 2