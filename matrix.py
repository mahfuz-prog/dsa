# diagonal sum

def diagonal_sum(arr):
	s1, s2 = 0, 0
	ptr1, ptr2 = 0, len(arr)-1
	for row in arr:
		s1 += row[ptr1]
		s2 += row[ptr2]
		ptr1 += 1
		ptr2 -= 1

	return s1, s2

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(diagonal_sum(arr))

# =========================================================================
# 74. Search a 2D Matrix (leetcode 74)
'''
You are given an m x n integer matrix matrix with the following two properties:

> Each row is sorted in non-decreasing order.
> The first integer of each row is greater than the last integer of the previous row.
'''
def searchMatrix_I(matrix, target):
	start = 0
	end = len(matrix) - 1
	
	# binary search on every row of matrix to identify target row
	while start <= end:
		mid = int(start + (end - start) / 2)
		val = matrix[mid][-1]
		if target > val:
			start = mid + 1
		elif target < val:
			end = mid - 1

		# check the possible target value inside this row
		if target >= matrix[mid][0] and target <= matrix[mid][-1]:
			# binary search to check if the target exist
			import bisect
			idx = bisect.bisect_left(matrix[mid], target)
			if len(matrix[mid]) > idx and matrix[mid][idx] == target:
				return True
			return False
	return False



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60],[63,67,68,75],[80,85,90,95]]
target = 5
# print(searchMatrix_I(matrix, target))





# =============================================================
# 240. Search a 2D Matrix II (leetcode 240)
def searchMatrix_II(matrix, target):

	# Time complexity O(m + n)
	# when m and n are similar in size or 
	# when m is much larger than n

	# m, n = len(matrix), len(matrix[0])
	# row, column = 0, n - 1
	# while row < m and column >=0:
	# 	if target == matrix[row][column]:
	# 		return True
	# 	elif target < matrix[row][column]:
	# 		column -= 1
	# 	else:
	# 		row += 1
	# return False


	# ============================================
	# Time complexity O(m * log(n))
	# Use when n is very large compared to m.
	import bisect
	for row in matrix:
		idx = bisect.bisect_left(row, target)
		if len(row) > idx and row[idx] == target:
			return True
	return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22]]
target = 5
print(searchMatrix_II(matrix, target))