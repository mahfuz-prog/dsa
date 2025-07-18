import time

'''
Modular Exponentiation
3^23 mod 7 = 6
when 3^23 is divided by 7, the remainder is 6

3^101101 / 3^23

3^1
S> 3^1 * 3^1 = 30^10 		->	 3^2 -> (3 * 3) % 7 = 2
S> 3^10 * 3^10 = 30^100 	->	 3^4 -> (2 * 2) % 7 = 4
M> 3^100 * 3^1 = 30^101 	->	 3^5 -> (4 * 3) % 7 = 5
.
.
.
.								-> 					= 2
M> 3^101100 * 3^1 = 30^101101 	->	 3^45 -> (2 * 3) % 7 = 6(Ans.)
'''

def modular_exponentiation(base, exp, mod):
	exp_bin = []
	while exp > 0:
		exp, rem = divmod(exp, 2)
		exp_bin.append(rem)

	rem = base
	# start calculation from 2nd bit
	exp_bin.pop()
	while exp_bin:
		_bin = exp_bin.pop()
		if _bin == 1:
			# squere and multiply
			rem = (rem * rem) % mod
			rem = (base * rem) % mod

		# squere if the bit is 0
		rem = (rem * rem) % mod

	return rem


base = 23
exp = 373
mod = 747
start_time = time.time()

# print(pow(base, exp, mod))
print(modular_exponentiation(base, exp, mod))

print(f"Execution time: {time.time()-start_time:.6f} seconds")