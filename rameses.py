import time
import collections
import math

start_time = time.clock()
initial_state = 'xx.....x...x...x'
GRID = 4
if collections.Counter(initial_state)['x']%2 == 0:
    MAX = 'odd'
else:
    MAX = 'even'

def actions(state):
    positions = []
    for i in range(0, len(state)):
        temp_list = list(state)
        if temp_list[i] != 'x':
 #           temp_list[i] = 'x'
            positions.append(i)
    return tuple(positions)

def result(state,position):
    temp_list = list(state)
    temp_list[position] = 'x'
    return ''.join(temp_list)


def eval_fun(state, position):   
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
#        print "Col" + columns
        diag1 = diag1 + state[GRID * (i / GRID) + i / GRID]
        diag2 = diag2 + state[(GRID - 1) * (i / GRID + 1)]
        if columns == 'x' * GRID:
            return 1
#    print diag1
#    print diag2
    if diag1 == 'x' * GRID or diag2 == 'x' * GRID:
        return 1
    min_max = 1
    state_matrix = []
    if position % GRID == 0:
        row = position / GRID - 1
        column = GRID - 1
    else:
        row = int(math.ceil(position / GRID))
        column = position % GRID - 1
    
    # print row,column
    #state_matrix[row][column] = 'x'
    for i in range(0, len(state), GRID):
        # print str(i)+" "+state[i:i+GRID]+" "+str(i+GRID)
        state_matrix.append(state[i:i + GRID])
    min_max += collections.Counter(state_matrix[row])['.']
    # print min_max
    j = GRID - 1
    for i in range(0, GRID):
        # print state_matrix[i][column]
        min_max += collections.Counter(state_matrix[i][column])['.']
        # print min_max
        if row == column or row + column == GRID - 1:
            if state_matrix[i][i] == '.' and i != row and j != column:
                min_max += 1
            if state_matrix[i][j] == '.' and i != row and j != column:
                min_max += 1
        j -= 1
    # return state_matrix

    return min_max


def cutoff_test(state,position):
    if eval_fun(state, position) in [-1,1]  or (time.clock() - start_time >= 5):
        return True

def argmin(seq, fn):
    """Return an element with lowest fn(seq[i]) score; tie goes to first one.
    >>> argmin(['one', 'to', 'three'], len)
    'to'
    """
    best = seq[0]; best_score = fn(best)
    for x in seq:
        x_score = fn(x)
        if x_score < best_score:
            best, best_score = x, x_score
    return best
def argmax(seq, fn):
    """Return an element with highest fn(seq[i]) score; tie goes to first one.
    >>> argmax(['one', 'to', 'three'], len)
    'three'
    """
    return argmin(seq, lambda x: -fn(x))


def min_max_search(state):
    #children = successors(state)

    def max_value(state, position = 1):
        if cutoff_test(state,position):
            if (collections.Counter(state)['x']%2 !=0 and MAX=='even') or (collections.Counter(state)['x']%2 ==0 and MAX=='odd'):
                return eval_fun(state, position)
            else:
                return -1 * eval_fun(state, position)
        v = -float("inf")
        for a in actions(state):
            v = max(v, min_value(result(state,a)))
        #if time.clock() - start_time <= 4.9:
        return v

    def min_value(state, position = 1):
        if cutoff_test(state,position):
            if (collections.Counter(state)['x']%2 !=0 and MAX=='even') or (collections.Counter(state)['x']%2 ==0 and MAX=='odd'):
                return eval_fun(state, position)
            else:
                return -1 * eval_fun(state, position)
        v = float("inf")
        for a in actions(state):
            v = min(v, max_value(result(state,a)))
        #if time.clock() - start_time <= 4.9:
        return v

    return argmax(actions(state), lambda a: min_value(result(state, a)))


# child = successors(initial_state)
# child = eval_fun(initial_state)
# print child
term_test = min_max_search(initial_state)
print term_test
print result(initial_state,term_test)
time.clock()
#print round(end_time - start_time, 5)
