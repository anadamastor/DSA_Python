# Check if an array contains a nnumber in Python
import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9])

def findNumber(array,number):
  for i in range(len(myArray)):
    if myArray[i] == number:
      return "Number found in index "  + str(i)
  return "Item not in array"

print(findNumber(myArray, 11))