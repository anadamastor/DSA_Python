
myDict1 = {"name":"ed", "age":23, "address":"london"}

# myDict.clear() #* Will empty dic

dict = myDict1.copy() #* creates a copy of the dictornary

#* fromkeys() return a new dictionary with the same value
myDict = {}.fromkeys([0,1,2,3], 0)
print(myDict) # > {0: 0, 1: 0, 2: 0, 3: 0}

#* get() return value of key, if not found will retunr the second par
print(myDict1.get("age", 27)) # > 23

#* items()
print(myDict1.items())
# > [('name', 'ed'), ('age', 23), ('address', 'london')]

#* keys()
print(myDict1.keys())
# > ['name', 'age', 'address']

#* popitem() return and remove an item from array
print(myDict1.popitem())

#* setdefault() returns value of key if in dictionary
#* or create it with the given value if not in dict
print(myDict1.setdefault("name","added"))
# > "ed"
print(myDict1.setdefault("name1","added"))
# > "added" (now we have a new key)

#* pop() will return the removed item if exists or second argument
print(myDict1.pop("name2","not in dic"))
# > "not in dic"

#* values() a list of values
print(myDict1.values())
# > "['ed', 23, 'added']"

#* update() updated dic from another dictioary elements or from 
#* an iterable of key value pair. Adds elements if key is not in dic
#* or updates it.
newDict = { "a": 1, "b": 2}
myDict.update(newDict)
print(myDict)