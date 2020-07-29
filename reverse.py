import pdb

# Given a 32-bit signed integer, reverse digits of an integer.

def reverse(num):
	rev = 0
	neg_flag = False
	if num < 0:
		num = abs(num)
		neg_flag = True
	while (num > 0):
		rev = rev*10 + num%10
		num = int(num/10)
	if rev > 2147483647:
	# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range
	# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
		return rev
	if neg_flag:
		rev = rev - rev - rev
	return rev

print(reverse(-321))