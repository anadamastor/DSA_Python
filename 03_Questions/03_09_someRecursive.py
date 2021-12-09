'''
Write a function called someRecursive which accetps an array and a callbacl
The functions returns true if a single value in the array returns true when
passed to the callback.
'''

def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, isOdd):
    if len(arr) == 1:
        return isOdd(arr[0])
    else:
        return isOdd(arr[0]) or someRecursive(arr[1:],isOdd)


print(someRecursive([1,2], isOdd))