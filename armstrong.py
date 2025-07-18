def is_armstrong(n):
	'''
	sum of every (digit ** count_of_digit) of a number == the number itself
	is a armstrong number
	Time Complexity: log(10base n)
	'''
	num = n
	res = 0
	power = len(str(n))
	while num > 0:
		num, digit = divmod(num, 10)
		res += digit ** power

	return True if res == n else False

# find all armstrong nums in n range
n = 1_000_000
for i in range(n):
	if is_armstrong(i):
		print("Armstrong Number:", i)