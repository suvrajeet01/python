#Lambda function or expresions
#python lambda function are nameless i.e. they donot have any name so are known as anonymous or nameless functions or more precisely a keyword

#uses
    #one time use - throw away function(needed only once as per requirement)
    #I/O of other function - used as either inputs ar returned as outputs of other higher order function
    #reduced code size - body of lambda function is written in single line

#writing anonymous function - lambda function is created using lambda operator
#syntax :- lambda arguments:expression      [lambda expression can take any number of arguments][all the argumennts or inputs muust be separated by a comma]

#lambda arguments : expression
x = lambda a:a*a        #nameless function so are assigned to a variable
print(x(3))
#OR
def new(a):
    return a*a
print(new(3))


#anonymous functions withinuser defined function
def A(X):
    return(lambda Y:X+Y)
t=A(4)
print(t(8))
u=A(7)
print(u(8))

#using lambda functions within filter(),map(),reduce() functions

#filter() function is used to filter iterables(lists,sets) using another function passed as an argument to test all elements to be either true or false and the output with true valuues is returned
#syntax of filter()
    #filter(function,iterables)
mylist1 = [1,2,3,4,5,6,7]
newlist1 = list(filter(lambda a:(a/3 == 2),mylist1))
print(newlist1)

mylist1 = [1,2,3,4,5,6,7]
newlist1 = list(filter(lambda a:(a%2 == 0),mylist1))
print(newlist1)

#map() function applies to all iterables and returns a new list
#syntax of map()
    #map(function,iterables)
mylist2 = [1,2,3,4,5,6,7]
l1 = list(map(lambda b:(b/3 !=2),mylist2))
print(l1)

#reduce() function applies some other function to a list of (iiterables) elements that are passed as parameter to it and finally returns a single value
#syntax of reduce()
    #reduce(function,sequence)
    #function libraries must be imported to use the reduce function
from functools import reduce
#alternatively import functools OR from functools import *
pbx1 = reduce(lambda a,b:a+b,[23,56,43,98,1])   #here 23+56 = x1;x1+43=x2;x2+98=x3;x3+1=fibal result=pbx1
print(pbx1)
