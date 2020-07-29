import pdb

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
# If the last word does not exist, return 0.
# Note: A word is defined as a maximal substring consisting of non-space characters only.

def lengthOfLastWord(s):
    if ' ' not in s:
    	result = len(s)
    else:
	    words = s.split(' ')
	    if len(words[len(words)-1]) == 0:
	    	words = words[:-1]
	    result = len(words[len(words)-1])
    return result
print(lengthOfLastWord("h "))