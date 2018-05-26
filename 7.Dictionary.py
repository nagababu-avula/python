# In Python dictionaries are like hash table data type
# A hash table consists of key value pairs
# Dictionaries are enclosed by curly braces { } and values can be assigned and accessed using square braces []

dict = {}
dict['abc'] = "This is abc"
dict['xyz'] = "This is xyz"
dict[9] = "number 9"

dict2 = {'name': 'naaga','id':1234, 'dept': 'IT Ops'}

print (dict['abc'])       # Prints value for 'abc' key
print (dict[9])           # Prints value for 9 key
print (dict2)             # Prints complete dictionary
print (dict2.keys())   # Prints all the keys
print (dict2.values()) # Prints all the values

#update dictionary
dict['abc'] ="This is updated"

del dict[9]

dict.clear()

del dict



