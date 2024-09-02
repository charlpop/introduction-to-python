# create a python class called car with two attributes:
#make and model. instantiate an object of the car class 
#print the make and model.


class Car:
 def __init__(self, make, model):
    self.make = make
    self.model = model

p1 = Car("Ford", "Mustang")
print(p1.make)
print(p1.model)
  