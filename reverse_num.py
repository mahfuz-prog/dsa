# Given a signed 32-bit integer n, return n with its digits reversed. 
# If reversing n causes the value to go outside the 
# signed 32-bit integer range [-2147483648, 2147483647], then return 0

def reverse_num(n):
	res = 0
	min_limit = -2**31
	max_limit = 2**31 - 1
	sign = 1 if n > 0 else -1

	while abs(n) > 0:
		# Div decrease the number 1digin from end. 112 / 10 == 11
		# Mod gives the last digit. 112 % 10 == 2
		n, digit = divmod(abs(n), 10)

		# check overflow
		# python variable can increase its size in runtime
		if res > int(max_limit / 10) or res < int(min_limit / 10):
			return 0

		# reverse the step to get result
		res = res * 10 + digit

	return res * sign

n = -214748364
print(reverse_num(n))