'''
1) divide number by 2
2) get the iteger quotient for next iteration
3) get the remainder for the binary digit
3)) repeat steps inti the quotiont is equal to 0

13 to binary
13/2 quotient 6 remainder 1
6/2 quotient 3 remainder 0
3/2 quotient 1 remainder 1
1/2 quotient 0 remainder 1

the results is 1101 (read from below)

10 to binary
10/2 quotient 5 remainder 0
5/2 quotient 2 remainder 1
2/2 quotient 1 remainder 0
1/2 quotient 0 remainder 1
10 in binary is 1010

'''

def decimal_to_binary(n):
  assert int(n) == n, "the numbers must integers only"
  if n == 0:
    return 0
  else:
    return n%2 + 10 * decimal_to_binary(int(n/2))  # need int for negatives WHY?

# tests
# print(decimal_to_binary(2))
print(decimal_to_binary(-2))
print(decimal_to_binary(1.2))

