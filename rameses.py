"""
We have used alpha-beta min_max algorithm to solve this problem. 
We calculate alpha-beta min_max value of a current state by counting to total number of empty spaces in the row, column and diagonal in which 'x' is added in current move.
"""
import time
import collections
import math
import sys
start_time = time.clock()
initial_state = sys.argv[2]
GRID = int(sys.argv[1])
TIME_LIMIT = float(sys.argv[3])

if len(initial_state) != GRID**2:
    print 'Enter appropriate value for GRID and INITIAL_STATE'
    exit()

#Decide which player will be MAX by checking who will have first turn depending of the initial state given in the input
if collections.Counter(initial_state)['x']%2 == 0:
    MAX = 'odd'
else:
    MAX = 'even'

def actions(state):
    #Return on posibble moves/actions from current state
    positions = []
    for i in range(0, len(state)):
        temp_list = list(state)
        if temp_list[i] != 'x':
            positions.append(i)
    return tuple(positions)

def result(state,position):
    #Return child node of current state if a 'x' is put in one of the possible positions
    temp_list = list(state)
    temp_list[position] = 'x'
    return ''.join(temp_list)


def eval_fun(state, position):

    #Check if any diagonal, column or row has all 'x', if yes return 1 as min_max value of the state
    diag1 = ''
    diag2 = ''
    for i in range(0, len(state), GRID):
        columns = ''
        if state[i:i + GRID] == 'x' * GRID:
            return 1
        for j in range(0, len(state), GRID):
            if j == '.':
                break
            columns = columns + state[i / GRID + j]
        diag1 = diag1 + state[GRID * (i / GRID) + i / GRID]
        diag2 = diag2 + state[(GRID - 1) * (i / GRID + 1)]
        if columns == 'x' * GRID:
            return 1
    if diag1 == 'x' * GRID or diag2 == 'x' * GRID:
        return 1

    #Find utility(min-max) value for the state which doesn't have all 'x's in any row, column and diagonal
    min_max = 0
    state_matrix = []
    if position % GRID == 0:
        row = position / GRID - 1
        column = GRID - 1
    else:
        row = int(math.ceil(position / GRID))
        column = position % GRID - 1

    for i in range(0, len(state), GRID):
        state_matrix.append(state[i:i + GRID])
    min_max += (collections.Counter(state_matrix[row])['.'] - collections.Counter(state_matrix[row])['x'])
    j = GRID - 1
    for i in range(0, GRID):
        min_max += (collections.Counter(state_matrix[i][column])['.'] - collections.Counter(state_matrix[row])['x'])
        if row == column or row + column == GRID - 1:
            if state_matrix[i][i] == '.' and i != row and j != column:
                min_max += 1
            if state_matrix[i][j] == '.' and i != row and j != column:
                min_max += 1
        j -= 1
    print min_max
    return min_max


def cutoff_test(state,position):
    #Cutoff the recursion for finding min-max value if the mentioned time limit is reached or terminal node has been reached
    if eval_fun(state, position) in [-1,1]  or (time.clock() - start_time >= TIME_LIMIT-0.5): #Adjusting time limit check to accomodate pre-calculations
        return True

def argmin(seq, fn):
    #Return an element with lowest fn(seq[i]) score; tie goes to first one.
    best = seq[0]; best_score = fn(best)
    for x in seq:
        x_score = fn(x)
        if x_score < best_score:
            best, best_score = x, x_score
    return best


def alphabeta_min_max_search(state):
    #Return the best  possible move for MAX player in given time limit depending on the given state

    print 'Thinking...'
    def max_value(state, alpha, beta, position = 1):
        if cutoff_test(state,position):
            #Return negative utility value is it's a move of MIN player or positive
            if (collections.Counter(state)['x']%2 !=0 and MAX=='even') or (collections.Counter(state)['x']%2 ==0 and MAX=='odd'):
                return eval_fun(state, position)
            else:
                return -1 * eval_fun(state, position)
        v = -float("inf")
        for a in actions(state):
            v = max(v, min_value(result(state,a),alpha,beta,a))
            if v>= beta:
                return v
            alpha = max(alpha,v)
        return v

    def min_value(state, alpha, beta, position = 1):
        if cutoff_test(state,position):
            #Return negative utility value if it's a move of MAX player or positive
            if (collections.Counter(state)['x']%2 !=0 and MAX=='even') or (collections.Counter(state)['x']%2 ==0 and MAX=='odd'):
                return -1 * eval_fun(state, position)
            else:
                return eval_fun(state, position)
        v = float("inf")
        for a in actions(state):
            v = min(v, max_value(result(state,a),alpha,beta,a))
            if v <= alpha:
                return v
            beta = min(beta,v)
        return v

    return argmin(actions(state), lambda a: -min_value(result(state, a),-float("inf"),float("inf")))

next_position = alphabeta_min_max_search(initial_state)
print 'Put Cross at position:'+str(next_position+1)
print result(initial_state,next_position)