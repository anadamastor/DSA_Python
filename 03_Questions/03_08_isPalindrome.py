'''
Recursive function which accepts a string and returns
true or false if string is palindrome.
'''

def isPalindrome(strng):
    if len(strng) == 1:
        return True
    if len(strng) == 2:
        return strng[0] == strng[-1]
    else:
        return strng[0] == strng[-1] and isPalindrome(strng[1:-1])

print(isPalindrome("awesome"))
print(isPalindrome("foobar"))
print(isPalindrome("tacocat"))
print(isPalindrome("amanaplanacanalpanama"))
print(isPalindrome("amanaplanacanlpandemonium"))


