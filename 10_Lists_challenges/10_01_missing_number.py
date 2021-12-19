# Find the missing number in an array of integer 1 to 100
array = list(range(101))
print(array)

# My solution______________________________
array.remove(2)
print(array)

for i in range(len(array)):
  if array[i] != i:
    print("missing number is " + str(i))
    break
  
# Official solution________________________
def find_missing(list , n):
  sum1 = 100*101/2 # calculation of n series
  sum2 = sum(list)
  print(sum1-sum2)

find_missing(array , 1)