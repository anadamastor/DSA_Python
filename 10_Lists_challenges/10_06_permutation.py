# 6 Permutation - same characters but in different orders

list_1 = [4,3,2]
list_2 = [2,3,1]

# First method - iterating through list 1
def check_permutation(list_1,list_2):
    if len(list_1) != len(list_2):
        return False
    for letter in list_1:
        if letter in list_2:
            output = True
        else:
            return False
    return output
print(check_permutation(list_1,list_2))

# second method, sorting lists and comparing them
def check_permutation_2(list_1,list_2):
    if len(list_1) != len(list_2):
        return False
    list_1.sort() # you need to sort before the comparison
    list_2.sort()
    return list_1 == list_2

print(check_permutation_2(list_1,list_2))
