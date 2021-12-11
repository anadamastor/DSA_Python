from array import *

#########################
# creation

arr1 = array ("i", [1,2,3,4,5])
arr2 = array ("d", [1.2, 1.3, 1.4])

# print(arr1)
# print(arr2)

#########################
# insertion

arr1.insert(0,7)
# print(arr1)

arr2.insert(0,7)
# print(arr2)

#########################
# traversing
# O(n) time complexity

def traverse_array(array):
  for i in array:
    print(i)

# traverse_array(arr1)

# #########################

# accessing an item in array
# O(1) time complexity
def access_element(array,index):
  if index >= len(array):
    print("There is not any element in this index")
  else:
    print(array)
    print(array[index])

# access_element(arr1,5)

#########################
# searching an item in array
# index, binary search, or loop in the array
def search_in_array(array, value):
  for i in array:
    if i == value:
      return array.index(value)
  return "the element does not exists in this array"
print(arr1)
# print(search_in_array(arr1 , 3))

#########################
# deletion
# O(1) if at the end
# O(n) if at any other plance
arr1.remove(4)
print(arr1)