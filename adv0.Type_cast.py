x = input()
print('Data type of x is :'+ type(y)) #check data type
# As we already mentioned by default input is a string

y = input('Enter an integer : ')  #Example '234'
print('Data type of y is :'+ type(y)) #check data type
z = int(y)
print('Data type of z is :'+ type(z)) #check data type


y = input('Enter a float : ')  #Example '2.44'
print('Data type of y is :'+ type(y)) #check data type
z = float(y)
print('Data type of z is :'+ type(z)) #check data type

s = 'abc 123 xyz 3.43'
t = tuple(s)
l = list(s)

s = 'k1 123 k2 abc k3 3.22'
d =dict(s)


