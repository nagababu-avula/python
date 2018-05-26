
# Updating Lists
lst = [1, 3, 5, 'naaga',3, 'Hi', 15.345]
print(lst)
print(lst[2])
print(lst[-2])
print(len(lst)) #max, min

lst.append('hello')
print(lst)

print(lst.count(3))

lst.insert(2, 'hello')
print(lst)

print(lst.sort())

print(lst.reverse())

#in tuples you can use len, max, min is possible
#sorting, reverse are not possible as tuples can not be updated.

dict = {}
dict['abc'] = "This is abc"
dict['xyz'] = "This is xyz"
dict[9] = "number 9"
len(dict)

str(dict)


