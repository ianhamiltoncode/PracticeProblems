import pdb

# Given a collection of distinct integers, return all possible permutations.

def permute(nums):
    n = len(nums)
    
    if n == 0:
        return []
    elif n == 1:
        return [nums]
    elif n == 2:
        return [nums, nums[::-1]]
    
    res = permute(nums[1:])
    ans = []
    
    num = nums[0]
    
    for arr in res:
        for i in range(0, len(arr)+1):
            tmp = arr[:]
            tmp.insert(i,num)
            ans.append(tmp)
        
    final_ans = []
    for i in ans:
    	if i not in final_ans:
    		final_ans.append(i)
    return final_ans

list1 = [1,1,2]
answer = permute(list1)
print(answer)