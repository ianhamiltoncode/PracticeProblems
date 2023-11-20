import pdb

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

def isValid(s):
	the_stack = []
	result = True
	for i in s:
		if i == '(' or i == '{' or i == '[':
			the_stack.append(i)
		elif i == ')':
			if len(the_stack) > 0:
				top = the_stack.pop()
				if top != '(':
					result = False
					break
			else:
				result = False
		elif i == '}':
			if len(the_stack) > 0:
				top = the_stack.pop()
				if top != '{':
					result = False
					break
			else:
				result = False
		elif i == ']':
			if len(the_stack) > 0:
				top = the_stack.pop()
				if top != '[':
					result = False
					break
			else:
				result = False
	if len(the_stack) > 0:
		result = False
	return result

#test

print(isValid('()'))
print(isValid('()[]{}'))
print(isValid('(]'))
print(isValid('([)]'))
print(isValid('{[]}'))
print(isValid('(('))
print(isValid(']'))