import pdb

# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

def romanToInt(s):
	i = len(s)-1
	number = 0
	while i >= 0:
		if s[i] == 'I':
			number += 1
		elif s[i] == 'V':
			if s[i-1] == 'I' and i > 0:
				number += 4
				i -= 1
			else:
				number += 5
		elif s[i] == 'X':
			if s[i-1] == 'I' and i > 0:
				number += 9
				i -= 1
			else:
				number += 10 
		elif s[i] == 'L':
			if s[i-1] == 'X' and i > 0:
				number += 40
				i -= 1
			else:
				number += 50
		elif s[i] == 'C':
			if s[i-1] == 'X' and i > 0:
				number += 90
				i -= 1
			else:
				number += 100
		elif s[i] == 'D':
			if s[i-1] == 'C' and i > 0:
				number += 400
				i -= 1
			else:
				number += 500
		elif s[i] == 'M':
			if s[i-1] == 'C' and i > 0:
				number += 900
				i -= 1
			else:
				number += 1000
		i -= 1
	return number

print(romanToInt('III'))
print(romanToInt('IV'))
print(romanToInt('IX'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))
print(romanToInt('MMMCDXC'))