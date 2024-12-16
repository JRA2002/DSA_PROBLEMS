# A recursive Python program 
# to check whether a given 
# number is palindrome or not

# A recursive function that 
# check a str[s..e] is 
# palindrome or not.
def isPalRec(st, s, e) :
	
	# If there is only one character
	if (s == e):
		return True

	# If first and last
	# characters do not match
	if (st[s] != st[e]) :
		return False

	# If there are more than 
	# two characters, check if 
	# middle substring is also 
	# palindrome or not.
	if (s < e + 1) :
		return isPalRec(st, s + 1, e - 1)

	return True

def isPalindrome(st) :
	n = len(st)
	
	# An empty string is 
	# considered as palindrome
	if (n == 0) :
		return True
	
	return isPalRec(st, 0, n - 1)


# Driver Code
st = "geeg"
if (isPalindrome(st)) :
	print("Yes")
else :
	print("No")
	
# This code is contributed
# by Nikita Tiwari.
