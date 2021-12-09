'''
Write a function called flatten which accetps an array and returns 
a new array with all values flattened

Extend adds the single elements of the argument, which in this 
case will be a recursion of the flatten function until the custItem
is not anymore a list.
'''
def flatten(arr):
    result_array = []

    for custItem in arr:
        if type(custItem) is list:
            result_array.extend(flatten(custItem))
        else:
            result_array.append(custItem)
    return result_array

print(flatten([0,1,2,[3,3]]))
