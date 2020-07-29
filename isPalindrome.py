import pdb

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

def isPalindrome(x):
	is_palindrome = False
	if x < 0:
		return is_palindrome
	rev = 0
	new_x = x
	while (new_x > 0):
		rev = rev*10 + new_x%10
		new_x = int(new_x/10)
	if rev == x:
		is_palindrome = True
	return is_palindrome

print(isPalindrome(-121))