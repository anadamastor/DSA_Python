# Find all pairs of an integer whose sum is qeual to number

myList = [1,2,3,4,5]
sum = 3

def pair_sum(myList, sum):
  print("This is Udemy exercise with lists")
  results = []
  for i in range(len(myList)):
    for j in range(i+1, len(myList)):
      if myList[i] + myList[j] == sum:
        results.append(f"{myList[i]}+{myList[j]}")
  return results
print(pair_sum(myList, sum))

# Leetcode mode
def pair_sum_leet(nums, target):
  print("This is leet code approach with lists (one return only one couple)")
  results = []
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        return i,j
  return results
print(pair_sum_leet(myList, sum))

def pair_sum_leet_dict(nums, target):
  dict_values = {}
  for num in nums:
    dict_values.setdefault(num,0)
    num2 = target - num
    if num2 in dict_values:
      index1 = nums.index(num)
      index2 = nums.index(num2)
      if index1 == index2:
        # 3 and 3 are the same when they have the same index
        continue
    return index1, index2