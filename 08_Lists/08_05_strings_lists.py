# strings and lists
# convert all chars in list
a = "spam"
b = list(a) # converts all letters in items of array
print(b)

# split (using space)
a = "spam spam spam"
b = a.split()
print(b)

a = "spam-spam-spam"
b = a.split("-") #using delimiter
print(b)

# list to string with joint
print('"-".join')
print(("-").join(b)) #this will convert list in string
