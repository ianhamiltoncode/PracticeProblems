import pdb

# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(nums):
	x = 0
	while(True):
		if x == len(nums):
			break
		if nums[x] == nums[x-1] and x != 0:
			nums.pop(x)
		else:
			x += 1
	return len(nums)

numbers = [1]
print(numbers)
print(removeDuplicates(numbers))
print(numbers)