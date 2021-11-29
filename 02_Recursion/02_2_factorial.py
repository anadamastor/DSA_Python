def factorial(n):
  # factorial is only calculated 
  # for positive numbers
  assert n >= 0 and int(n) == n, "The number must be positive integer only!"
  
  #base case - stopping criterion
  if n in [0,1]:
    return 1
  else:
    # recursive case
    return (n * factorial(n-1))

print(factorial(1.5))