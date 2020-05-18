#fancy decorators

#class decorator
class Square:
    def __init__(self,side):
        self.side = side
    @property       #decorator
    def side(self):
        return self._side
    @side.setter
    def side(self,value):
        if value >= 0 :
            self._side = value
        else:
            print('error')
    @property
    def area(self):
        return self._side **2
    @classmethod
    def unit_square(cls):
        return cls(1)

s = Square(int(input('Enter side of square ')))
print('side of square given = ',s.side)
print('Area of square with side',s.side,'is',s.area)