import pdb

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

def searchInsert(nums, target):
    flag = 0
    for x in range(len(nums)):
    	if nums[x] == target or nums[x] > target:
    		result = x
    		flag = 1
    		break
    if flag == 0:
    	result = len(nums)
    return result


nums = [1,3,5,6]
#pdb.set_trace()
print(searchInsert(nums, 0))