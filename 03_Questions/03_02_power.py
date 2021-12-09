'''
Calculate power of a number with recursion

9**3 = 9 * 9**2
						9**2 = 9 * 9
f(n**p) = f * f(n**(p-1))
'''

def power(base,exp):
  assert exp >= 0 and int(exp) == exp, "The exponent must be positive int only"
  if base == 0 :
    return base
  if exp == 0:
    return 1
  if exp == 1 :
    return base
  else:
    # if exp > 0:
    return base * power(base, exp-1)
    # elif exp < 0:
      # return base * power(base, exp+1)


print(power(-1,4)) #negative base
print(power(2.3,4)) # float base
print(power(1,-2)) # negative exp
print(power(1,2.2)) # non integer exp