# Lists operations

# + operator / Concatenation
a = [1,2,3,4]
b= [4,5,6]
c = a + b
print(c)

# * operator
a = [0]
a = a * 4
print(a) # repetas 0 for times [0, 0, 0, 0]

# Lists functions
a = [1,2,3,4]
print(len(a))

# maximum element in array
print(max(a))

# minimum element in array
print(min(a))

# sum for all items
print(sum(a))

# average of list
print(sum(a)/len(a))

# CLI average calculation
numbers = []
while True:
  inp = input("Enter a number: ")
  if inp == "done":
    break
  value = float(inp)
  numbers.append(value)
  average = sum(numbers) / len(numbers)
print("average:", average) # you can print multiple vars
