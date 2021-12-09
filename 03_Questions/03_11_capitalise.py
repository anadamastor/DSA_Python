'''
Recursive funtion that capitalises the first
letter of each string in the array
'''


def capitalizeFirst(arr):
  result = []
  if len(arr) == 0:
    return result
  result.append(arr[0][0].upper() + arr[0][1:])
  return result + capitalizeFirst(arr[1:])

print(capitalizeFirst(["text", "uno", "due"]))