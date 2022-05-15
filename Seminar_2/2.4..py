def isPalindrome(s):
    return s == s[::-1]
s = "Programming"
pal = isPalindrome(s)
if pal:
        print("True")
else:
    print(False)