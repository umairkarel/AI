"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0

    for row in board:
        for col in row:
            count += 1

    if count%2:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available = []
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                available.append((i,j))

    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    currPlayer = player(board)
    new_board = [[col for col in row] for row in board]
    i, j = action

    if board[i][j]:
        raise Exception
    else:
        new_board[i][j] = currPlayer

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in (X, O):
        # check vertical
        for row in board:
            if row == [player] * 3:
                return player

        # check horizontal
        for i in range(3):
            column = [board[x][i] for x in range(3)]
            if column == [player] * 3:
                return player
        
        # check diagonal
        if [board[i][i] for i in range(0, 3)] == [player] * 3:
            return player

        elif [board[i][len(board[0])-i-1] for i in range(0, 3)] == [player] * 3:
            return 


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return True if (winner(board) or actions(board) == []) else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)

    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -5
            for action in actions(board):
                minval = min_value(result(board, action))[0]
                if minval > v:
                    v = minval
                    optimal_move = action
            return v, optimal_move

    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = 5
            for action in actions(board):
                maxval = max_value(result(board, action))[0]
                if maxval < v:
                    v = maxval
                    optimal_move = action
            return v, optimal_move

    curr_player = player(board)

    if terminal(board):
        return None

    if curr_player == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]
