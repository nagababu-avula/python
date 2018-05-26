# Last section we discussed basic data types like numbers, float and string data types
# Now let us discuss more data types supported by python


# Let us start with Lists
# A list contains items separated by commas and enclosed within square brackets []
# To some extent, lists are similar to arrays, 
#the differences between them is that all the items belonging to a list can be of different data type.

arr = [2, 3, 4, 5, 6]
list1 = [1, 3, 5, 7, 9, 15]
list2 = [2, 3.1, 'naaga', 5, 4.2]


print (list1)          # Prints complete list
# in python array index start from 0 unlike in R language index start from 1
print (list1[0])       # Prints first element of the list
print (list1[1:3])     # Prints elements starting from 2nd till 3rd 
print (list1[2:])      # Prints elements starting from 3rd element
print (list1 * 2)  # Prints list two times
print (list1 + list2) # Prints concatenated lists

print(list2)
list2[2] = 4.34
print(list2)

del list2[3]
print(list2)

