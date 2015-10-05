import time
import collections
import math

start_time = time.clock()
initial_state = ".x......x"
GRID = 3


def successors(state):
    children = []
    for i in range(0, len(state)):
        temp_list = list(state)
        if temp_list[i] != 'x':
            temp_list[i] = 'x'
            children.append((''.join(temp_list), i))
    return children


def eval_fun(state, position):
    state_matrix = []
    if position % GRID == 0:
        row = position / GRID - 1
        column = GRID - 1
    else:
        row = int(math.ceil(position / GRID))
        column = position % GRID - 1
    min_max = 0
    # print row,column
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


def terminal_test(state):
    diag1 = ''
    diag2 = ''
    for i in range(0, len(state), GRID):
        columns = ''
        if state[i:i + GRID] == 'x' * GRID:
            return 0
        for j in range(0, len(state), GRID):
            if j == '.':
                break
            columns = columns + state[i / GRID + j]
        print "Col" + columns
        diag1 = diag1 + state[GRID * (i / GRID) + i / GRID]
        diag2 = diag2 + state[(GRID - 1) * (i / GRID + 1)]
        if columns == 'x' * GRID:
            return 0
    print diag1
    print diag2
    if diag1 == 'x' * GRID or diag2 == 'x' * GRID:
        return 0
    if time.clock() - start_time == 4.9:
        return True


def min_max_search(state):
    children = successors(state)

    def max_value(state, position):
        if terminal_test(state):
            return eval_fun(state, position)
        if terminal_test(state) == 0:
            return 0
        v = -float("inf")
        for a in successors(state):
            v = max(v, min_value(a[0], a[1]))
        return v

    def min_value(state, position):
        if terminal_test(state):
            return -1 * eval_fun(state, position)
        if terminal_test(state) == 0:
            return 0
        v = float("inf")
        for a in successors(state):
            v = min(v, max_value(a[0], a[1]))
        return v

    return max_value(children[0][0],children[0][1])


# child = successors(initial_state)
# child = eval_fun(initial_state)
# print child
term_test = min_max_search(initial_state)
print term_test
time.clock()
print round(end_time - start_time, 5)
