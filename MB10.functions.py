# Call a function to seperate a block of code for particular task / for repetitive task
def sayhi():
  print("Hi, Everybody.")
  return

for i in range(10):
  sayhi()


# Arguments passing
def add(x, y):
  z = x + y
  print("Addition : ", z)
  return
  
add(2, 3)


# Arguments passing by variables
def add(x, y):
  z = x + y
  return z
  
a = 2
b = 3
c = add(a, b)
print("Addition : ", c)



# Argument passing by reference #by default in python
def modify(x):
  x[1] = 3.87
  return x
  
lst = [2, 3, 4]
modify(lst)
print("Updated List : ", lst)



