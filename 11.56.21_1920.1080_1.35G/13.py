#nested loop 2
#program to print pythagorean numbers between a particular range of numbers using nested for loop
#the integers satisfying the relation a^a + b^b = c^c

from math import sqrt
n = int(input('Maximum Number? '))
for a in range(1,n+1):                              #will not include n+1
    for b in range(a,n):                            #will not include n
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if ((c_square - c**2) == 0):
            print(a,b,c)