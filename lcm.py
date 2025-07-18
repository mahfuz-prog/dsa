# calculate gcd
def calclulate_gcd_euclid_rec(a, b):
	# Assume a > b
	if b == 0:
		return a
	return calclulate_gcd_euclid_rec(b, a % b)

# least common multiple (LCM)
#  lcm = (a * b) / gcd(a, b)
def calculate_lcm(a, b):
	return int(a * b / calclulate_gcd_euclid_rec(a, b))

a = 26
b = 701
print(calculate_lcm(a, b))