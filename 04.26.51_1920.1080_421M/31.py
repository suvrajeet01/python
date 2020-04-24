#classes and objects
    #extremely powerful
    #makes program more useful and organised
    #major data types includes :-strings,numbers,booleans
    #objects and classes helps create one's own data types that can't be represented using the present or predefined data types
    #with class one can define it's own data type

#creating student object(actual student with information)
#object is the actual data type
#object is just a instance of class
#class is like a overall template that defines a data type
#object is actual data type with information or data

from student import student     #tells the program to import student class from student file;the first student refers to the filename and the second one refers to the class

#creating student
#creating object of the class just like normal variables
student1 = student('Edward', 'Computer Science' , 3.7, False)   #student1 is a student object
student2 = student('George', 'Information Security' , 3.0, True)
print(student1.name)     #all the attributes of student1 object can be accessed from inside of this object
print(student1.gpa)
print(student2.gpa)

#when student1 and student2 varaibles were created and student class was called __init__ function was called
    #the values of name,major,etc are passed onto the class named student onto the __init__ function