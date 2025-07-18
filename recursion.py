'''
n = 5
stack1 rec_I(n) print(5) rec_I(5-1) => waiting print(5, 'hola')
stack2 rec_I(4) print(4) rec_I(4-1) => waiting print(4, 'hola')
stack3 rec_I(3) print(3) rec_I(3-1) => waiting print(3, 'hola')
stack4 rec_I(2) return

stack3 print(3, 'hola')
stack2 print(4, 'hola')
stack1 print(5, 'hola')
'''
def rec_I(n):
	if n == 2:
		return
	print(n, id(n))
	rec_I(n-1)
	print(n, id(n), 'hola')

n = 5
# rec_I(n)

# ==============================================
# ==============================================
'''
n = 5
stack1 rec_I(n) print(5) rec_I(5-1)
stack2 rec_I(4) print(4) rec_I(4-1)
stack4 rec_I(3) return 3 => print(3)
'''
def rec_II(n):
	if n == 3:
		return n

	print(n, id(n))
	return rec_II(n-1)

n = 5
# print(rec_II(n))


# ==============================================
# ==============================================
# fact(n) = n x (n-1) x (n-2) x (n-3) x (n-4)
# fact(5) = 5 x 4 x 3 x 2 x 1
'''
stack1 return 5 * waiting fact(5-1)
stack2 return 4 * waiting fact(4-1)
stack3 return 3 * waiting fact(3-1)
stack4 return 2 * waiting fact(2-1)
stack5 return 1

stack4 return 2 * 1
stack3 return 3 * 2
stack2 return 4 * 6
stack1 return 5 * 24
print(120)
'''
def factorial(n):
	if n == 0 or n == 1:
		return 1
	return n * factorial(n-1)

n = 5
# print(factorial(n))


# ==============================================
# ==============================================
def n_sum(n):
	if n == 1:
		return 1

	return n + n_sum(n-1)

n = 4
# print(n_sum(n))


'''
fibonacci number
==============================================
0 > 0
1 > 1
2 > [0, 1] = 1
3 > [1, 1] = 2
4 > [1, 2] = 3
5 > [2, 3] = 5
6 > [3, 5] = 8
7 > [5, 8] = 13
==============================================
'''
def fibonacci(n):
	if n == 0 or n == 1:
		return n

	base = [0,1]
	for _ in range(n-1):
		base[0], base[1] = base[1], sum(base)

	return base[1]



# for i in range(10):
# 	print(i, '=', fibonacci(i))



'''
==============================================
Binary Search
'''
def bin_search(arr, target, start, end):
	# base case
	if start <= end:

		# logic
		mid = (start+end) >> 1
		val = arr[mid]

		if val == target:
			return val, mid
		elif target > val:
			return bin_search(arr, target, mid+1, end)
		elif target < val:
			return bin_search(arr, target, start, mid-1)
	
	return -1


arr = [1,2,3,4,5,6,7,8]
start = 0
end = len(arr)-1
# print(bin_search(arr, 4, start, end))



'''
==============================================
all subset

Recursive
'''

subsets = []
def find_subset(nums, i, ans):
	if i == len(nums):
		subsets.append(list(ans))
		return

	# include
	ans.append(nums[i])
	find_subset(nums, i+1, ans)

	ans.pop()

	# skip duplication if the next element is same
	idx = i+1
	while idx < len(nums) and nums[idx] == nums[idx-1]:
		idx += 1

	# exclude
	find_subset(nums, idx, ans)

	return subsets

nums = sorted([1, 2, 2, 3])
ans = []
# print(find_subset(nums, 0, ans))


'''
==============================================
N-Queens

Recursive - Rowwise
Time complexity O(n!)
'''

# check the queen is not in a attacking position
def is_valid(board, row, col, n):
	# check column, we don't need to check after the given row because we haven't 
	# place a Q after the row
	for i in range(row):
		if board[i][col] == "Q":
			return False

	# check right diagonal, i--, j++
	# end of board could be identified by colum max and row 0 
	i, j = row, col
	while i >= 0 and j < n:
		if board[i][j] == "Q":
			return False
		i -= 1
		j += 1

	# check left diagonal, i--, j--
	# end of board could be identified by row 0 and col 0
	i, j = row, col
	while i >= 0 and j >= 0:
		if board[i][j] == "Q":
			return False
		i -= 1
		j -= 1

	return True

# recursive function
def backtrack(board, row, n):
	# base case
	if row == n:
		res.append([''.join(row) for row in board])
		return

	# choices for every column of given row
	for col in range(n):
		if is_valid(board, row, col, n):
			# if not attacking place a queen there
			board[row][col] = "Q"

			# recursive call for next row
			backtrack(board, row+1, n)

			# if the function backtracking than remove the queen
			board[row][col] = "."

	return res

n = 4
res = []
board = [['.'] * n for _ in range(n)]
# print(backtrack(board, 0, n))


'''
==============================================
N-Queens - all possible solution count

Recursive - column wise
Time complexity O(n!)
'''
def is_valid(board, row, col, n):
	# check any other queen in the given row
	for i in range(col):
		if board[row][i] == "Q":
			return False

	# top left diagonal
	i, j = row, col
	while i >= 0 and j >= 0:
		if board[i][j] == "Q":
			return False
		i -= 1
		j -= 1

	# bottom left diagonal
	i, j = row, col
	while i < n and j >= 0:
		if board[i][j] == "Q":
			return False
		i += 1
		j -= 1

	return True

def backtrack(board, col, n):
	# base case
	if col == n:
		return 1

	count = 0
	# choices for every row of given column
	for row in range(n):
		if is_valid(board, row, col, n):
			# if queens are not attacking than place the queen
			board[row][col] = "Q"

			# recursive call for next column
			count += backtrack(board, col+1, n)

			# if the function backtrack than remove the queen
			board[row][col] = "."

	return count

n = 4
board = [['.'] * n for _ in range(n)]
# print(backtrack(board, 0, n))


'''
==============================================
Knight Tour Configuration

time complexity O(n^2)
'''
def is_valid(grid, n, row, col, move):
	# 8 possible move
	moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
	for i, j in moves:
		i, j = row + i, col + j
		# 0 <= i < n and 0 <= j < n and grid[i][j] == move:
		if i >= 0 and i < n and j < n and j >= 0 and grid[i][j] == move:
			return i, j

	return False


def knight_tour(grid, n, row, col, move):
	if move > n * n - 1:
		return True

	next_move = is_valid(grid, n, row, col, move)
	if next_move:
		i, j = next_move
		return knight_tour(grid, n, i, j, move+1)
	else:
		return False

n = 5
grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
# print(knight_tour(grid, n, 0, 0, 1))

'''
==============================================
sudoke solver

Time complexity O(9^empty space)
'''
def is_valid(board, row, col, target):
	# check row and column
	for i in range(9):
		if board[row][i] == target or board[i][col] == target:
			return False

	# check squere
	row_start, col_start = (row // 3) * 3, (col // 3) * 3
	for i in range(3):
		for j in range(3):
			if board[row_start+i][col_start+j] == target:
				return False

	return True

# solution 1 ====================================
def sudoku_solver_I(board, row, col):
	# base case
	if row == 9:
		return True

	# handle cell position
	next_row, next_col = row, col + 1
	if next_col == 9:
		next_row += 1
		next_col = 0

	# for non empty cell call the function for next cell
	# without puting the anythin on board
	if board[row][col] != '.':
		return sudoku_solver_I(board, next_row, next_col)

	# this will apply for only empty cell
	for i in map(str, range(1, 10)):
		if is_valid(board, row, col, i):
			board[row][col] = i

			# if true return from base case
			if sudoku_solver_I(board, next_row, next_col):
				return True

			# backtrecking step
			board[row][col] = '.'

	print(board)


# solution 2 ====================================
def sudoku_solver_II(board):
	for i in range(9):
		for j in range(9):
			# if empty
			if board[i][j] == '.':
				# try to put 1-9 in this cell
				for k in map(str, range(1, 10)):
					# check a valid value for this position
					if is_valid(board, i, j, k):
						# if possible put it
						board[i][j] = k

						if sudoku_solver_II(board):
							return True

						# backtreck for bad choice
						board[i][j] = '.'

				# ===============================================================================
				# this is where magic happening
				# ===============================================================================
				print(board)

				# If no number works, return False (trigger backtracking)
				return False

	# If no empty cells are left, the board is solved
	return True

board = [
	["5","3",".",".","7",".",".",".","."],
	["6",".",".","1","9","5",".",".","."], 
	[".","9","8",".",".",".",".","6","."],
	["8",".",".",".","6",".",".",".","3"],
	["4",".",".","8",".","3",".",".","1"],
	["7",".",".",".","2",".",".",".","6"],
	[".","6",".",".",".",".","2","8","."],
	[".",".",".","4","1","9",".",".","5"],
	[".",".",".",".","8",".",".","7","9"]
]

# board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
# print(sudoku_solver_I(board, 0, 0))
# sudoku_solver_II(board)
# print(board)


'''
==============================================
Rat in maze
'''
ans = []
def rat_in_maze(maze, row, col, n, path=''):
	# base case
	if row < 0 or col < 0 or row >= n or col >= n or maze[row][col] == 0 or maze[row][col] == -1:
		return

	# ans
	if row == n - 1 and col == n - 1:
		ans.append(path)
		return 

	# mark as a visited cell
	maze[row][col] = -1

	# right move
	rat_in_maze(maze, row, col + 1, n, path+"R")
	# left move
	rat_in_maze(maze, row, col - 1, n, path+"L")
	# up move
	rat_in_maze(maze, row - 1, col, n, path+"U")
	# bottom move
	rat_in_maze(maze, row + 1, col, n, path+"D")

	# backtrecking 
	maze[row][col] = 1

maze = [[1,1,1,0,1],[1,0,1,1,1],[0,0,1,1,1],[1,0,0,1,1],[1,0,0,0,1]]

n = len(maze)

# edge case
if maze[0][0] == 0 or maze[n-1][n-1] == 0:
	print('error')

# rat_in_maze(maze, 0, 0, n)
# print(ans)


'''
==============================================
combination sum
'''

res = set()
def helper(candidates, idx, target, combination=[]):
	if idx == len(candidates) or target < 0:
		return

	if target == 0:
		res.add(tuple(combination))
		return
	
	c = candidates[idx]
	combination.append(c)

	# single inclusion
	helper(candidates, idx+1, target-c, combination)

	# multiple inclusion
	helper(candidates, idx, target-c, combination)

	# exclude
	# backtrecking
	combination.pop()
	helper(candidates, idx+1, target, combination)



candidates = [2,3,5]
target = 8
# helper(candidates, 0, target)
# print(res)


'''
==============================================
Palindrome Partitioning
time complexity O(n x 2^n)
'''
res = []
def is_palindrome(s):
	if s == s[::-1]:
		return True

def pali_parti(s, part=[]):
	if len(s) == 0:
		res.append(part.copy())

	for idx, i in enumerate(s, start=1):
		cut = s[0:idx]
		if is_palindrome(cut):
			part.append(cut)
			pali_parti(s[idx:len(s)])
			part.pop()


s = 'aab'
# pali_parti(s)
# print(res)