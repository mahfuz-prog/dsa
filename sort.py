'''
==============================================
merge 2 sorted list
'''
def merge(lst1, lst2):
	temp = []
	i, j = 0, 0
	while i < len(lst1) and j < len(lst2):
		if lst1[i] <= lst2[j]:
			temp.append(lst1[i])
			i += 1
		else:
			temp.append(lst2[j])
			j += 1

	# for remaining lst1 elements
	while i < len(lst1):
		temp.append(lst1[i])
		i += 1

	# for remaining lst2 elements
	while j < len(lst2):
		temp.append(lst2[j])
		j += 1

	print(temp)
	# return temp


lst1 = [1,5,8,9]
lst2 = [3,4,5]
# print(merge(lst1, lst2))


'''
==============================================
merge sort

O(nlogn)
'''
def merge(arr, start, mid, end):
	temp = []
	i, j = start, mid+1
	while i <= mid and j <= end:
		if arr[i] <= arr[j]:
			temp.append(arr[i])
			i += 1
		else:
			temp.append(arr[j])
			j += 1

	# for remaining lst1 elements
	while i <= mid:
		temp.append(arr[i])
		i += 1

	# for remaining lst2 elements
	while j <= end:
		temp.append(arr[j])
		j += 1

	# storing the temp value to the main array
	for idx, val in enumerate(temp):
		arr[idx+start] = val

def merge_sort(arr, start, end):
	if start < end:
		mid = (start+end)//2
		# left part
		merge_sort(arr, start, mid)

		# right part
		merge_sort(arr, mid+1, end)
		merge(arr, start, mid, end)

arr = [9,3,7,5,6,4,8,2]
n = len(arr)
# merge_sort(arr, 0, n-1)
# print(arr)

'''
==============================================
quick sort - pivit as the last element
Time complexity O(n logn)

but if the pivit is smallest of largest in this array
Worst case -> Time complexity is O(n^2)
'''

def partition(arr, start, end):
	# choose pivit and return its index
	# modify in original array
	idx = -1
	for i in range(end):
		if arr[i] <= arr[end]:
			idx += 1
			arr[idx], arr[i] = arr[i], arr[idx]

	idx += 1
	arr[idx], arr[end] = arr[end], arr[idx]
	return idx

def quick_sort(arr, start, end):
	if start < end:
		pivit_idx = partition(arr, start, end)

		# left half start from 0 to (pivit_idx-1)
		quick_sort(arr, start, pivit_idx-1)

		# right half
		quick_sort(arr, pivit_idx, end)
	

arr = [9,3,7,5,6,4,8,2]
n = len(arr)
# quick_sort(arr, 0, n-1)
# print(arr)