
myDict1 = {"one":"uno", "two": "dos", "three":"tres"}

#* in operator
print("uno" in myDict1)
# > False

print("uno" in myDict1.values())
# > True


#* for operator: visits each pair
for key in myDict1:
  print(key, myDict1[key])
# O(n) time complexity.

#* all() : return true if all methods are true
print(all(myDict1)) # true for empty dictionary

#* any() returns true if at least one value is true.
print(any(myDict1)) # false for empy dictionary

#* len() returns a number of pairs
print(len(myDict1))
# > 3

#* sorted return a sorted list from the items.
# sort(iterable, reverse_par(boolean), key (function that sorts))

myDict2 = {"ea": 1, "eea": 2, "urewwr": 3}
print(sorted(myDict2))
# > ['ea', 'eea', 'urewwr']
print(sorted(myDict2, reverse= True))
# > ['urewwr', 'eea', 'ea']

print(sorted(myDict2, key = len))
# > ['ea', 'eea', 'urewwr']

