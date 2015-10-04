import time
import collections
start_time = time.clock()
initial_state = ".x......x"
GRID = 3

def successors(state):
	children = []	
	for i in range(0,len(state)):	
		temp_list = list(state)	
		if temp_list[i] != 'x':
			temp_list[i] = 'x'
			children.append((''.join(temp_list),i))
	return children

def eval_fun(state,position):
	state_matrix = []
	column = position/GRID + 1
	min_max = 0
	row = position%GRID
	for i in range(0,GRID):
		print state[i:i+GRID]
		state_matrix.append(state[i:i+GRID])
	min_max += collections.Counter(state_matrix[column-1]+state_matrix[row-1])['.']
		if row == column:
			for i in range(0,GRID):
				if state_matrix[i][i] == '.':
					min_max += 1
	return state_matrix		


def min_max_search(state):
	c = collections.Counter(state)
	if c['x']%2 == 0:
		p = 1
		print 'Player 1 move:'
	else: 
		p = 2
		print 'Player 1 move:'
child = successors(initial_state)
#child = eval_fun(initial_state)
print child
end_time = time.clock()
print round(end_time - start_time,5)