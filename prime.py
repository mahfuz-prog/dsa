def is_prime(n):
	'''
	>> Prime number > 1
	>> only two distinct factor 1 and itself
	>> factor always lies  between 2 -> root(n)
	'''
	if n < 2:
		return False

	# int(n ** 0.5) + 1 (the square root of n, rounded up) and +1 for inclusive range
	for i in range(2, int(n ** 0.5) + 1):
		# find factor
		if n % i == 0:
			return False
	return True


# identify Prime and Non Prime number
for i in range(20):
	if is_prime(i):
		print("Prime:", i)