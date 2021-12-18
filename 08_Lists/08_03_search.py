# searching for an element in ind the liS
my_list = [10,20,30,40,50,60]

# IN operator

if 20 in my_list:
  print(my_list.index(20))
else: 
  print("Value not in the list")

# O(N) time complexity - checks elements one by one

# LINEAR SEARCH - O(n) time complexity
print("----LINEAR SEARCH------")
def search_in_list(list,value):
  for i in list:
    if i == value:
      return list.index(value)
  return "Value not in list"

print(search_in_list(my_list,20))