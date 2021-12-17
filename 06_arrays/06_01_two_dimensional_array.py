import numpy as np

twoArray = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(twoArray)

# will print
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# insertion
# axis 1 is columen, axis 0 is row

# addign a column O(n):
new_two_dim_array_column = np.insert(twoArray, 0, [[10,10,10]], axis = 1)
print(new_two_dim_array_column)

# addin a row O(n):
new_two_dim_array_row = np.insert(twoArray, 0, [[10,10,10]], axis = 0)
print(new_two_dim_array_row)

# append to add row/column or column at the end - O(1)
new_Array = np.append(twoArray, [[10,10,10]], axis = 0)
print(new_Array)

# Accessing an element of Two Dimensional Array
def access_element(array,row_index,col_index):
  if row_index >= len(array) or col_index >= len(array[0]):
    print("incorrect index")
  else:
    print(array[row_index][col_index])

print(twoArray)
access_element(twoArray,1,1)

# Traversing two dimensional  array
print("array traversing")
def traverse(array):
  for i in range (len(array)): # numbers of rows
    for j in range(len(array[0])): # number of colums
      print(array[i][j]) # for each row we are traversing all columns
traverse(twoArray)
# prin takes constant time complexity.

# Searching for an element in two dim arrays
print("Searching for an element in two dim arrays")
# using linear search: search for every elemnt until it finds what we are looking for
def searchTwoDimArray(array, value):
  print(f"you are looking for {value}")
  for i in range(len(array)):
    for j in range(len(array[0])):
      if array[i][j] == value:
        return f"the value is located at index {i} {j}"
  return "the element is not found"

print(twoArray)
print(searchTwoDimArray(twoArray, 44))

# delete column or row in two dim arrays
print("Delete column or row in two dim arrays")
# we use numpy for that, axis 0 is row an 1 is column. THe first
# number identifies the number of row/column to delete
new_two_dim_array = np.delete(twoArray, 1, axis = 0) # 
print(twoArray)
print("deleting a row")
print(new_two_dim_array)