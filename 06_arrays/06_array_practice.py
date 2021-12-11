from array import *

# 1. create array and traverse
# O(n) time complexity
my_array = array("i", [1,2,3,4,5] )
print("STEP 1")
for i in my_array:  
  print(i)

# 2. accessing elements through indexes
print("STEP 2")
print(my_array[0])

# 3. Append any value with append() > only at the end
print("STEP 3")
my_array.append(2)
print(my_array)

# 4. insert value in  array
# time consuming process > shifts all items
print("STEP 4 - insert()")
my_array.insert(0,11)
print(my_array)

# 5. extend() method with more than one value from array
print("STEP 5 - extend()")
my_array1 = array("i", [10,11,23])
my_array.extend(my_array1)
print(my_array)

# 6. fromlist() - adding items from list instead of array
print("STEP 6 - fromlist()")
tempList = [20,21,22,23]
my_array.fromlist(tempList)
print(my_array)

# 7. remove() - will remove the first occurence of the argument 
# O(n) - time consuming
print("STEP 6 - remove() and pop()")
my_array.remove(22)
print(my_array)

# 8. pop() - will remove the first occurence of the argument 
print("STEP 8 - pop()")
my_array.pop()
print(my_array)

# 9. find element throught its index 
print("STEP 9 - index() ")
print(my_array.index(21))

# 10. reverse 
print("STEP 10 - reverse() ")
my_array.reverse()
print(my_array)

# 11. get buffer information 
print("STEP 11 - buffer_info() ")
print(my_array.buffer_info())

# 12. number of occurrences
print("STEP 12 - count(11) ")
print(my_array.count(11))

# 13. convert array to string 
print("STEP 13 - tostring() ")
strTemp = my_array.tostring()
print(strTemp)
ints = array("i")
ints.fromstring(strTemp)
print(ints)

# 14. convert array to list 
print("STEP 14 - tolist() ")
print(my_array.tolist())
# array output:
# array('i', [21, 20, 23, 11, 10, 2, 5, 4, 3, 2, 1, 11])
# list output
# [21, 20, 23, 11, 10, 2, 5, 4, 3, 2, 1, 11]

# 15. Slice
print("STEP 15 - slice ")
print(my_array[1:4])
