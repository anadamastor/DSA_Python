
def productOfArray(arr):
    '''
    arr[0] * arr[1:]
            arr[1:] = arr[1] * arr[2:]
    '''

    if len(arr) == 1:
        return arr[0]

    return arr[0] * productOfArray(arr[1:])

print(productOfArray([1,2,3,2]))
