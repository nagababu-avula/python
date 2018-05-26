# Call a function to seperate a block of code for particular task / for repetitive task
def sayhi():
  print("Hi, Everybody.")

for i in range(10)
  sayhi()


# Arguments passing by value
def add(x, y):
  z = x + y
  print("Addition : ", z)
  
add(2, 3)


# Arguments passing by reference
def add(x, y):
  z = x + y
  print("Addition : ", z)
  
a = 2
b = 3
add(a, b)


# return a value from function
def multiply(a,b):
  x = a * b
  return x
  
a = 2
b = 3
c = multiply(a, b)
print("Multiplication : ", c)



