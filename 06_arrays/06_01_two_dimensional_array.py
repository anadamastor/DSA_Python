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