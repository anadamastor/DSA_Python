# Find the duplicate numbers in a given array

myList = [1,2,3,2,4,5,6]

def removeDuplicates(myList):
    output = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] != myList[j]:
                if myList[i] not in output:
                    output.append(myList[i])   
                elif myList[j] not in output:
                    output.append(myList[j])     
    return output
    
print(removeDuplicates(myList))

# Course solution
# def removeDuplicates(myList):
#     new_list=[]
    
#     for i in myList:
    
#         if i not in new_list:
    
#             new_list.append(i)
    
#     return new_list