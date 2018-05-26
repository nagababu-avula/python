class Student:
  count = 0  # Class variable
  dept = ''
  
  def __init__(self, sid, sname):
    self.id = sid
    self.name = sname
    Student.count += 1
  
  def disp(self):
    print("id :", self.id, "Name :", self.name)
    
  def department(marks):
    if marks > 80:
      self.dept = "Computers"
    elif marks > 60:
      self.dept = "IT"
    else
      self.dept = "Software"
      
    return
    
s1 = Student(1001, 'Naaga')
s2 = Student(1002, 'Chris')
s3 = Student(1003, 'Sara')

s1.disp()
s2.disp()
s3.department(78)

print("Student Name and Department are : ", s3.name, s3.dept)

print("Total no of students : ", Student.count)



