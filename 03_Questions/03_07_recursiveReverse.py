'''
Recursive function which accepts a string and returns
a new string in reverse
'''

def reverse(strng):
    if len(strng) == 1:
        return strng
    else:
        return reverse(strng[1:]) + strng[0] # this order is important

print(reverse("hello"))