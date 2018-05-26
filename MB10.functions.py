# Call a function
def sayhi():
  print("Hi, Everybody.")

sayhi()


# Arguments passing
def add(a,b):
  c = a + b
  print("Addition : ", c)
  
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



