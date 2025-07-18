# GCD (Greatest Common Divisor) or HCF (Highest Common Factor)
# ===================================================
# bruteforce approach
def calclulate_gcd(a, b):
	if a == 0:
		return b

	if b == 0:
		return a

	if a == b:
		return a

	res = 1
	# gcd range shoud be 1 to minimum of a, b
	# Time Complexity O(min(a, b))
	for i in range(1, (min(a, b) + 1)):
		if (a % i) == 0 and (b % i) == 0:
			res = i
	return res

# Euclid's Algorithm
# ===================================================
# gcd(a - b, b), if a > b
# gcd(a, b - a), if a < b

# optimization
# gcd(a % b, b), if a > b
# gcd(a, b % a), if a < b
def calclulate_gcd_euclid(a, b):
	while a > 0 and b > 0:
		if a > b:
			a = a % b
		else:
			b = b % a

	if a == 0:
		return b
	return a


# Euclid's Algorithm recursion
# ===================================================
# gcd(a % b, b), if a > b
# gcd(a, b % a), if a < b
def calclulate_gcd_euclid_rec(a, b):
	# Assume a > b
	if b == 0:
		return a
	return calclulate_gcd_euclid_rec(b, a % b)


a = 26
b = 900
print(calclulate_gcd(a, b))
# print(calclulate_gcd_euclid(a, b))
# print(calclulate_gcd_euclid_rec(a, b))