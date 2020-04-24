#class functions
#a function that can be used inside a class that can either modify the objects of the class or give specific informationn about objects
from student1 import student1

student11 = student1('Oscar', 'Accounting', 3.1)
student12 = student1('Phyllis', 'Business', 3.8)

print(student11.on_honor_roll())
print(student12.on_honor_roll())