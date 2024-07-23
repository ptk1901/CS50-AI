#"""
#Tic Tac Toe Player
#"""
#from math import inf
##import math
#import copy
#
#X = "X"
#O = "O"
#EMPTY = None
#action_set = set()
#
#
#def initial_state():
#    """
#    Returns starting state of the board.
#    """
#    return [[EMPTY, EMPTY, EMPTY],
#            [EMPTY, EMPTY, EMPTY],
#            [EMPTY, EMPTY, EMPTY]]
#
#
#def player(board):
#    """
#    Returns player who has the next turn on a board.
#    """
##if terminal(board) == False:
#    counter = 0
#    for row in range(3):
#        for column in range(3):
#            if board[row][column] != EMPTY :
#                counter += 1
#    if counter%2 == 0:
#        return X
#    else:
#        return O
##else:
#    #return None
#        
#
#    #raise NotImplementedError
#
#
#def actions(board):
#    """
#    Returns set of all possible actions (i, j) available on the board.
#    """
##if terminal(board) == False:
#    actions = set()
#    for row in range(3):
#        for column in range(3):
#            if board[row][column] == EMPTY:
#                actions.add((row,column))
#                action_set.add((row,column))
#    return actions
##else:
##    return None
#    #print(f"{actions}")
##raise NotImplementedError  
#
#
#def result(board, action):
#    """
#    Returns the board that results from making move (i, j) on the board.
#    """
#    action_possible = action_set
#    if action in action_possible:
#        current_player = player(board)
#        new_board = copy.deepcopy(board)
#        new_board[action[0]][action[1]] = current_player
#        print(f"{new_board}")
#        print(f"{board}")
#        return new_board
#    else:
#        raise Exception("Not a valid move!")
#
#    
#
#    #raise NotImplementedError
#
#
#def winner(board):
#    """
#    Returns the winner of the game, if there is one.
#    """
#    #if terminal(board) == True:
#    for column in range(3):
#        if board[0][column] == board[1][column] == board[2][column]:
#            print(f"{board[0][column]}")
#            return board[0][column]
#    for row in range(3):
#        if board[row][0] == board[row][1] == board[row][2]:
#            print(f"{board[row][0]}")
#            return board[row][0]
#    if board[0][0] == board[1][1] == board[2][2]:
#        print(f"{board[0][0]}")
#        return board[0][0]
#    if board[0][2] == board[1][1] == board[2][0]:
#        print(f"{board[0][2]}")
#        return board[0][2]
#    else:
#        return None
#    #else:
#    #        return None
#
#    #raise NotImplementedError
#
#
#def terminal(board):
#    """
#    Returns True if game is over, False otherwise.
#    """
#    if winner(board) != None:
#        return True
#    if any(EMPTY in sublist for sublist in board):
#        return False
#    else:
#        return True
#    #raise NotImplementedError
#
#
#def utility(board):
#    """
#    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
#    """
#    if winner(board) == X:
#        return 1
#    if winner(board) == O:
#        return -1
#    if winner(board) == None:
#        return 0
#    
#    #raise NotImplementedError
#
#def max_value(board):
#    if terminal(board) == True:
#        return utility(board)
#    v = float(-inf)
#    for action in action_set:
#        v = max(v, min_value(result(board,action)))
#    return v
#
#def min_value(board):
#    if terminal(board) == True:
#        return utility(board)
#    v = float(inf)
#    for action in action_set:
#        v = min(v,max_value(result(board,action)))
#    return v
#
#
#def minimax(board):
#    """
#    Returns the optimal action for the current player on the board.
#    """
#
#    #raise NotImplementedError


"""
Tic Tac Toe Player
"""
from math import inf
#import math
import copy

X = "X"
O = "O"
EMPTY = None
action_set = set()


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
    if terminal(board) == False:
        counter = 0
        for row in range(3):
            for column in range(3):
                if board[row][column] != EMPTY :
                    counter += 1
        if counter%2 == 0:
            return X
        else:
            return O
    else:
        return None
        

    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board) == False:
        actions = set()
        for row in range(3):
            for column in range(3):
                if board[row][column] == EMPTY:
                    actions.add((row,column))
                    action_set.add((row,column))
        return actions
    else:
        return None
    #print(f"{actions}")
#raise NotImplementedError  


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    action_possible = actions(board)
    if action in action_possible:
        current_player = player(board)
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = current_player
        print(f"{new_board}")
        return new_board
    else:
        raise Exception("Not a valid move!")

    

    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column]:
            if board[0][column] == EMPTY:
                continue
            return board[0][column]
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[0][column] == EMPTY:
                continue
            return board[row][0]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    if any(EMPTY in sublist for sublist in board):
        return False
    else:
        return True
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    if winner(board) == None:
        return 0
    
    #raise NotImplementedError

def max_value(board):
    if terminal(board) == True:
        return utility(board)
    v = float(-inf)
    for action in actions(board):
        if v==1:
            break
        v = max(v, min_value(result(board,action)))
    print(f"value of v is {v}")
    return v

def min_value(board):
    if terminal(board) == True:
        return utility(board)
    v = float(inf)
    for action in actions(board):
        if v==-1:
            break
        v = min(v,max_value(result(board,action)))
    print(f"value of v is {v}")
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board)== X:
        plays = []
        for action in actions(board):
            plays.append((min_value(result(board, action)), action))
        return sorted(plays, key = lambda x: x[0], reverse= True)[0][1]
    elif player(board)== O:
        plays = []
        for action in actions(board):
            plays.append((max_value(result(board, action)), action))
        return sorted(plays, key = lambda x: x[0])[0][1]
    #raise NotImplementedError
