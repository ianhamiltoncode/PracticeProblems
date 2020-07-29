import pdb

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

def longestSequence(input_list):
	result_list = []
	input_list.sort()
	list_len = len(input_list)
	if list_len < 2:
		return list_len
	else:
		j = 0
		for x in range(0, list_len - 1):
			result_list.append(1)
			if abs(input_list[x]-input_list[x-1]) == 1:
				result_list[j]+=1
			else:
				j+=1
	result = max(result_list)
	return result

testing = longestSequence([100, 4, 200, 1, 31, 2, 5])
print(testing)