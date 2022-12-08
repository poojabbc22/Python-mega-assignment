
def isPalindrome(s):
	return s == s[::-1]
s = "madam"
ans = isPalindrome(s)

if ans:
	print(s,"is a palindrome")
else:
	print("No")
