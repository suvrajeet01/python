#map,filter,reduce functions enables the functional programming(outputs depends solely on the arguments passed) aspect of python
#map() function applies a given function to all iterables and returns a new list
#filter() function creates output list consisting of values for which function returns true
#reduce() function applies to the iterables and returns a single value

#map() function
#map(function,iterables)
def new(a):
    return a*a
x=map(new,[1,2,3,4])
print(x)
print(list(x))
x1 = map(new,[1,2,3,4])
print(tuple(x1))
x2 = map(new,[1,2,3,4])
print(set(x2))
#map() function can also take more than one list of parameter as argument
def new(a,b):
    return a*b
x=map(new,[1,2,3,4],[5,6,7,8])
print(x)
print(list(x))
#lambda with map()
lst = [1,2,3,4,5]
y=list(map(lambda x:x+3,lst))
print(y)


#filter() function
#filter(function,iterables)
def new1(i):
    if i>=3:
        return i
j = filter(new1,(1,2,3,4,5,6,7))
print(j)
print(tuple(j))
#filetr with lambda
z=filter(lambda x: (x>=3),(1,2,3,4,5,6,7))
print(list(z))


#reduce() function
#reduce(function,iterables)
from functools import reduce
def a(x,y):
    return x+y
s = reduce(a,[1,2,3,4,5,6,7,8])
print(s)
#reduce with lambda
print(reduce(lambda q,p:q*p,[1,2,3,4,5,6,7,7]))


#filter() within map()
c=map(lambda x:x+x,filter(lambda x:(x>=4),[2,3,4,5,6]))
print(tuple(c))

#map() within filter()
d=filter(lambda x:(x>=4),map(lambda x:x+x,[2,3,4,5,6]))
print(set(d))

#map() & filter() within reduce()
r = reduce(lambda x,y:x+y, map(lambda x:x+x, filter(lambda x: (x<=4),[1,2,3,4,5,6,7])))
print(r)