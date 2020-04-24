#another class to model another type of chef
#model same as chef but with extra functions defined in it
#instead of copy and paste, the class can be inherited using parenthesis and the name of the class whose attributes are to be inherited
#also import is required
from chef import chef
class chineseChef(chef):
    def make_special_dish(self):
        print('The chef makes orange chicken')      #overwriting a inherited function for a new class
    def make_fried_rice(self):
        print('The chef makes fried rice')
