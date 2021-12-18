my_list = [1,2,3,4,]

print(my_list)

my_list.insert(0,11) #at the beginning
print(my_list)
# O(n) time complexity, every time we add we need to move
# all elements right

my_list.append(222) #at the end
print(my_list)
# O(1) time complexity

new_list = [22,23,24]
my_list.extend(new_list)
print(my_list)
# O(n) time complexity