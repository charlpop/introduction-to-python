class Person:
  def __init__(self, fname, lname, age):
    self.firstname = fname
    self.lastname = lname
    self.age = age

  def printname(self):
    print(self.firstname, self.lastname, self.age)

class Student(Person):
  def __init__(self, fname, lname, age):
    Person.__init__(self, fname, lname, age)

x = Student("Mike", "Olsen", 50)
x.printname()
