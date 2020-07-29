import pdb

# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(needle, haystack):
	result = 0
	h_len = len(haystack)
	n_len = len(needle)
	if needle not in haystack or n_len > h_len:
		result = -1
	elif n_len == 0:
		result = 0
	else:
		for x in range(h_len):
			if haystack[x] == needle[0]:
				cut_str = haystack[x:]
				if len(cut_str) > n_len:
					cut_str = cut_str[:n_len-len(cut_str)]
				if cut_str == needle:
					result = x
					break
	return result

#pdb.set_trace()
#print(strStr('ll', 'hello'))
print(strStr('pi', 'mississippi'))
#print(strStr('aa', 'aaa'))