import pdb

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
	prefix = ''
	for i in range(len(strs)):
		if i == 0:
			prefix = strs[i]
		else:
			if len(strs[i]) < len(prefix):
				str_cmp_len = len(strs[i])
			else:
				str_cmp_len = len(prefix)
			if str_cmp_len == 0:
				prefix = ''
				break
			for j in range(str_cmp_len):
				if strs[i][j] != prefix[j]:
					prefix = strs[i][:j]
					break
				if j == str_cmp_len - 1:
					if len(strs[i]) <= len(prefix):
						prefix = strs[i]

	return prefix

#print(longestCommonPrefix(['flower', 'flow', 'flower']))
#print(longestCommonPrefix(['dog', 'racecar', 'car']))
#pdb.set_trace()
print(longestCommonPrefix(['aaa', 'aa', 'aaa']))
print(longestCommonPrefix(['abab', 'aba', '']))
#pdb.set_trace()
print(longestCommonPrefix(['ab', 'abcc']))