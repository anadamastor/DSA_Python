# Find the missing number in a given array

totalCount = 10
myList = list(range(1,totalCount+1))
num_to_remove = 3
myList.remove(num_to_remove)

def missingNumber(myList, totalCount):
    print(myList)
    for index, num in enumerate(myList):
        print(index,num)
        if index+1 != num:
            return f"missing number is: {num-1}"

print(missingNumber(myList,totalCount))