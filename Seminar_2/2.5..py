def isPalindrome(s):
    return s == s[::-1]
s = "Programming"
pal = isPalindrome(s)
s = s.lower()

if s == s[::-1]:
        print("The string cited is an palindrome")
else:
        print("The palindrome cited is not an palindrome")