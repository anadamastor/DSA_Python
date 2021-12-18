
my_list = ["a","b","c","d","e"]

print(my_list[0:2]) # second index is not included (2-1)
print(my_list[1:]) # all elements from 1
print(my_list[:]) # all elements

#'updating multiple elements with slice'
my_list[0:2] = ["x","y"]
print(my_list)

my_list.pop(1) # if not index is provided the
#last element is deleted
print(my_list)
# O(n) time complexity - time consuming

#if we do not need the deleted valute use delete()
del my_list[1]
print(my_list)

# you an delete using slicing as well
del my_list[0:2]
print(my_list)

# my_list = ["a","b","c","d","e"]
# if you want to remove a specific known element
my_list.remove("e")
print(my_list)
# O(n) time complexity - time consuming

