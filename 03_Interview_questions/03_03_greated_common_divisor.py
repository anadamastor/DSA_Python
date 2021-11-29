'''
# largest positive divisor whitout a remainder
gcd(8,12) = 4
using prime factorization
8 = 2 * 2 * 2
12 = 2 * 2 * 3

Euclidean algorithm
gcd(48,18)
1# 48/12 = 2 remainder 12
2# 18/12 = 1 remainder 6
3# 12/6 = 2 remainder 0

gcd(a,0) = a
gcd(a,b) = gcd(b, a mod b)

'''

def gcd(a,b):
  assert int(a) == a and int(b) == b, "the numbers must integers only"
  if a < 0:
    a *= -1
  if b < 0:
    b *= -1
  if b == 0: # prevents 0 division
    return a
  else:
    return gcd(b, a % b)

# tests
print(gcd(48,18))
print(gcd(3,6))
print(gcd(-3,6))
print(gcd(3,-6))
print(gcd(0,6))
print(gcd(3,0))