#inheritance in python
#inheritance is where we can define bunch of attributes and functions and other things inside of a class and inerit all of those attributes to another class
#ie.e having all the functionalities of one class in another without having to write all the same attributes and methods

from chef import chef
from chineseChef import chineseChef

myChef = chef()         #making chef object
myChef.make_chicken()
myChef.make_special_dish()
myChef.make_salad()

mychineseChef = chineseChef()   #defining or making chinese chef object
mychineseChef.make_special_dish()
mychineseChef.make_fried_rice()
mychineseChef.make_chicken()