# Traversing a dictionary

mydict = {"name":"ed", "age":23, "address":"london"}

def traverseDict(mydict):
    for key in mydict:
        print(key, mydict[key])

traverseDict(mydict)

def searcDict(mydict, value):
    for key in mydict:
        if mydict[key] == value:
            return key, value
    return "key not here"

print(searcDict(mydict, "ed"))

#* Delete an elemente from a dictionary

mydict.pop("name")
print(mydict)

print(mydict.popitem())
print(mydict)

print(mydict.clear())
print(mydict)

#! delete one key/value pair
del mydict["age"]

