# only handle positive number
# to convert 50 in base-10 to base-2:

# 50 / 2 = 25; 50 % 2 = 0
# 25 / 2 = 12; 25 % 2 = 1
# 12 / 2 = 6; 12 % 2 = 0
# 6 / 2 = 3; 6 % 2 = 0
# 3 / 2 = 1; 3 % 2 = 1
# 1 / 2 = 0; 1 % 2 = 1

def int_to_bin(n):
	'''
	number if binary digit of a decimal is (log(2^n) + 1)
	'''
	n_bin = ''
	while n > 0:
		n, mod = divmod(n, 2)
		n_bin = str(mod) + n_bin

	return n_bin

n = 50
calculated_bin = int_to_bin(n)
print(f'int({n}) = bin({calculated_bin})')

print(f'32bit: {calculated_bin:0>32} -> int({n})')
print(f'32bit: {n:032b} -> int({n})\n')


# =================================================
# convert the decimal number 0.6875 to binary:

# 0.6875 × 2 = 1.375 with integer 1
# 0.375 × 2 = 0.75 with integer 0
# 0.75 × 2 = 1.5 with integer 1
# 0.5 × 2 = 1 with integer 1

def float_to_bin(n):
	'''
	number if binary digit of a decimal is (log(2^n) + 1)
	'''
	n_bin = ''
	while n != 0:
		temp = n * 2
		n = temp - int(temp)
		n_bin += str(int(temp))

	return n_bin

# 125.125
# Answer 1111101.001
# 125.6875
# ans 1111101.1011
res = int_to_bin(125) + "." + float_to_bin(.6875)
print(res)