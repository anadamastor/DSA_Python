# Two sum

# Checking if i + j (which is i+1) equals to target
def find_pairs(nums, target):
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] == nums[j]:
        continue
      elif nums[i] + nums[j] == target:
        print(f"index {i} = {nums[i]}, index {j} = {nums[j]}")

mylist= [ 1,2,3,3,3,4,4,5]
target = 6
find_pairs(mylist, target)