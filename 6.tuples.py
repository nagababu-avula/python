# A tuple is another sequence data type that is similar to the list. 
# A tuple consists of a number of values separated by commas. 
# Unlike lists, however, tuples are enclosed within parenthesis ().

# The main difference between lists and tuples are − 
# Lists are enclosed in square brackets [ ] and their elements and size can be changed, 
# while tuples are enclosed in parentheses ( ) and cannot be updated once it is initialized. 
# Tuples can be thought of as read-only lists.

tuple1 = ( 'abcd', 786 , 2.23, 'naaga', 70.2  )
tuple2 = (123, 'naaga')

print (tuple1)           # Prints complete tuple
print (tuple1[0])        # Prints first element of the tuple
print (tuple1[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple1[2:])       # Prints elements starting from 3rd element
print (tuple2 * 2)       # Prints tuple two times
print (tuple1 + tuple2)  # Prints concatenated tuple
