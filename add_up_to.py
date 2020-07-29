import pdb

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def add_up_to(the_l, k):
	placeholder = [-1] * len(the_l)
	for i in range(len(the_l)):
		if the_l[i] <= k:
			placeholder[i] = k - the_l[i]
		if i > 0:
			for x in range(i):
				if the_l[i] == placeholder[x] and placeholder[x] != -1:
					return True
	return False

test = [7, 16, 3, 11, 100]
print(add_up_to(test, 17))