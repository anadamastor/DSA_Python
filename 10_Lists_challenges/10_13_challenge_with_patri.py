
my_array = [1,1,2,2,3,4,4]
my_array_2 = [1,1,2,2,3,3,4,4,4,5,6,7]

def singleNumber(nums):
  freq_vec = {}
  for i in range(len(nums)):
    freq_vec.setdefault(nums[i], 0)
    freq_vec[nums[i]] += 1
  print(min(freq_vec, key=freq_vec.get))


singleNumber(my_array)
singleNumber(my_array_2)