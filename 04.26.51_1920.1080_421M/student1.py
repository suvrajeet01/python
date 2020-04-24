class student1:
    def __init__(self, name1, major1, gpa1):
        self.name1 = name1
        self.major1 = major1
        self.gpa1 = gpa1

#defining function inside a class that can be accessed by all objects of the class
#i.e. creating a on_honor_roll function inside student1 class that can be accessed by all student1 objects
#function that provides service to the objects of the class
    def on_honor_roll(self):
        if self.gpa1 >= 3.5:
            return True
        else:
            return False