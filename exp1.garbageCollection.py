
class Student:
  count = 0  # Class variable
  
  def __init__(self, sid, sname):
    self.id = sid
    self.name = sname
    self.dept = ''
   
    Student.count += 1
  
  def disp(self):
    print("id :", self.id, "Name :", self.name)
    
  def __del__(self):
    class_name = self.__class__.__name__
    print (class_name, "destroyed")

    
s1 = Student(1001, 'Naaga')
s1.disp()
del s1


import Student
s1 = Student.Student()

