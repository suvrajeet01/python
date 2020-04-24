#creating student data type
#creating a class for student:-student class
#class defines what a data type is OR just a overview of the data


class student:
    def __init__(self, name, major, gpa, is_on_probation):      #student data type with the attributes
        self.name = name        #name of actual object = name casted ; self.name is attribute of student
        self.major = major      #student is storing major
        self.gpa = gpa          #student is storing gpa,etc
        self.is_on_probation = is_on_probation
            #templates for what a student data type is....
            #name, major, gpa,etc are just the values inside __init__ function OR are just parameters
            #self refers to actual object
