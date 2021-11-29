'''
SUMS OF DIGITS OF POSITIVE INTEGER WITH RECURSION

# by diving by ten we get the digits of any number
10 => 1 + 0 = 1
(10 / 10 => 1) + (10 % 10 => 0) = 1

111 => 3
[(111/10 => 11)] + (111 % 10 => 1)
# call recursion on 11 here
[(11 / 10 => 1) + (11 % 10 => 1) = 1]
[ 1 + 1 ] + 1 => 3

so finally it becomes:
f(n) = n%10 + f(n//10)
'''

def sum_of_digits(digit):
  assert digit >= 0 and int(digit) == digit, "Only >= 0 numbers" 
  if digit == 0:
    return digit
  else:
    return (sum_of_digits(digit // 10) + digit % 10)


print(sum_of_digits(101))