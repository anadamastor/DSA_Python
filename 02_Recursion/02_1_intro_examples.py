def recursive_method(n):
  if n < 1:
    print("n is less than 1")
  else:
    recursive_method(n-1)#
    print(n)

recursive_method(10)

# prints:
# n is less than 1
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10