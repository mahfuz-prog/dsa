import sys
import time
sys.set_int_max_str_digits(10000000)
sys.setrecursionlimit(20000)

# efficient approach than bruteforce
def calculate_power(a, b):
	'''
	if b is even
		a^b = (a^2)^b/2

	if b is odd
		a^b = a * a^(b-1)
	'''
	res = 1
	while b > 0:
		# odd number
		# Last bit / least significant bit (LSB) is 1 of a odd number
		# bitwise and operation of number with 1, give 1 if the number is odd
		# or if the number is even give 0.
		if (b&1):
			res *= a

		a = a * a
		# right shift by k bits is equivalent to dividing the number by 2^k
		# left shift by k bits is equivalent to multiplying the number by 2^k
		b = b >> 1

	return res

# recursive
# =========================================
def power_recursive(a, b):
	if b < 0:
		raise ValueError("Exponent must be non-negative for this implementation")

	# Base case: any number to the power of 0 is 1
	if b == 0:
		return 1

	# Recursive case: a^b = a * a^(b-1)
	return a * power_recursive(a, b - 1)


a, b = 566, 4999
start_time = time.time()

# print(pow(a, b))
# print(calculate_power(a, b))
# print(power_recursive(a, b))

print(f"Execution time: {time.time()-start_time:.6f} seconds")