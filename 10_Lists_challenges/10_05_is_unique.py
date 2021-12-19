# Implement alg to determin if a list as all unique characters.

my_list = [1,3,45,6,7,8,4,2]

print("First Approach")
def is_unique(my_list):
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i] == my_list[j]:
                return False
    return True

print(is_unique(my_list))

# Different approach
print("Second Approach")
def is_unique_dos(my_list):
    check_arr = []
    for i in range(len(my_list)):
        if i in check_arr:
            return False
        else:
            check_arr.append(my_list[i])
    return True

print(is_unique_dos(my_list))
