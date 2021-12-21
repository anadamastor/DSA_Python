# given a list write a function to get first,second best scorest
# from the list

my_list = [84,85,86,87,90]

def first_second(givenList):
    first, second = 0, 0

    for i in range(len(givenList)):

        print(my_list[i])

        if givenList[i] > first:
            second = first
            first = givenList[i] 

        print(f"first is {first}, second is {second}")

    return(first,second)

print(first_second(my_list))
