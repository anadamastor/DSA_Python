# 6 Permutation - same characters but in different orders

list_1 = [1,3,2]
list_2 = [2,3,1]

# def check_permutation(list_1,list_2):
#     if len(list_1) != len(list_2):
#         return False
#     output = False
#     for letter_1 in list_1:
#         if letter_1 in list_2:
#             output = True
#         else:
#             output = False
#     return output
# print(check_permutation(list_1,list_2))

def check_permutation_2(list_1,list_2):
    if len(list_1) != len(list_2):
        return False
    list_1.sort() # you need to sort before the comparison
    list_2.sort()
    return list_1 == list_2

print(check_permutation_2(list_1,list_2))
