import pdb

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def two_sum(nums, target):
	answer = (None, None)
	for i in range(len(nums)):
		if i > 0:
			for x in range(i):
				if nums[i] + nums[x] == target:
					answer = (x, i)
	return answer

test = [2, 7, 11, 15]
#test = [-1, -2, -3, -4, -5]
print(two_sum(test, 9))