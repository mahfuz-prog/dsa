# get bit ==========================
n, i = 5, 2
print(f"Bit at {i}:", int(bin(n)[-i]) ^ 1)

# other way
bit_mask = 1 << i
ith_bit = n & bit_mask

if ith_bit:
	print(f"Bit at {i}: 1")
else:
	print(f"Bit at {i}: 0")


# set bit ==========================
n, i = 5, 1

bit_mask = 1 << i
bit_set = n | bit_mask
print(f"Set bit at {i}: {n:b} -> {bit_set:b}")


# clear bit ==========================
n, i = 7, 1

bit_mask = 1 << i
# not with bit mas
bit_mask = ~bit_mask
bit_set = bit_mask & n
print(f"Clear bit at {i}: {n:b} -> {bit_set:b}")


# update bit =================================
# update ith bit to 1
n, i = 7, 1
bit_mask = 1 << i
bit_mask = ~bit_mask
bit_set = bit_mask & n
print(f"Updated bit at {i}, to 1: {n:b} -> {bit_set:b}")

# update ith bit to 0
n, i = 5, 1
bit_mask = 1 << i
bit_set = n | bit_mask
print(f"Updated bit at {i}, to 0: {n:b} -> {bit_set:b}")


# addition without +, - operator =========================
a = 5
b = 6

mask = 0xfff
while (mask & b) > 0:
    """
        Shifting this result left by 1 moves 
        the carry to the correct bit position 
        for the next addition.
    """    
    carry = (a & b) << 1

    # update a with the xor for the next addition with carry
    a = a ^ b

    # update b with carry for next addition untill b is 0
    b = carry

print((mask & a) if b > 0 else a)