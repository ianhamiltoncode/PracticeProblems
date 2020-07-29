import pdb

# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

def removeElement(nums, val):
	while(True):
		try:
			nums.remove(val)
		except ValueError:
			break
	return len(nums)

numbers = [1, 1]
print(numbers)
print(removeElement(numbers, 1))
print(numbers)