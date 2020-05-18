#generator used to genarate iterables
#generators are functions that return traversable objects and produce items one at a time only when required
#generators run along for loop

#generators vs normal functions
    #make use of yield keyword instead of return keyword
    #runs when next() method is called instead of name of the method
    #prodeces one item at a timeand only when required instead of all items at once

#creating/writing generators
def new(dict):
    for x,y in dict.items():
        yield x,y
a = {
    1:'Hi',
    2:'Welcome'
}
b=new(a)   #generator object for function
print(b)
print(next(b))
print(next(b))

def myfunc(i):
    while i <=3:
        yield i
        i+=1
j=myfunc(2)     #creating generator object
print(next(j))
print(next(j))

def ex():
    n=3
    yield n
    n = n*n
    yield n
v = ex()
print(next(v))
print(next(v))

#generators with loops - executig same functions at once
def ex():
    n=3
    yield n
    n = n*n
    yield n
v = ex()
for x in v:
    print(x)

#generator expressions along with for loop produces iterators
#list comprehensions are reassembled anonymous generator functions are created like lambda functions
f=range(6)
print('list comprehension',end=':')
q=[x+2 for x in f]
print(q)
print('generator expression',end=':')
r=(x+2 for x in f)
print(r)
for x in r:
    print(x)

print('generator expression',end=':')
r=(x+2 for x in f)
print(r)
print(min(r))

#use cases
#1.generating fibonacci series - a series of number where in each number also known as fibonacci number is the sum of two preceding numbers
def fib():
    f,s=0,1
    while True:
        yield f
        f,s=s,f+s
for x in fib():
    if x>50:
        break
    print(x,end=' ')

#2.generating a number stream(stream of numbers)
a=range(100)
b=(x for x in a)
print(b)
for y in b:
    print(y)
#for even values
a=range(2,100,2)
b=(x for x in a)
print(b)
for y in b:
    print(y)
#for odd numbers
a=range(1,100,2)
b=(x for x in a)
print(b)
for y in b:
    print(y)

#3.generating the sinewave using Seaborn and generator
#using normal function
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
def s(flip = 2):
    x=np.linspace(0,14,200)
    for i in range(1,5):
        plt.plot(x,np.sin(x+i*.5)*(7-i)*flip)

sb.set()
s()
plt.show()
#using generator function
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
def s(flip = 2):
    x=np.linspace(0,14,100)
    for i in range(1,10):
        yield(plt.plot(x,np.sin(x+i*.5)*(7-i)*flip))

sb.set()
s=s()
plt.show()

print(next(s))
print(next(s))      #printing out another sine wave
print(next(s))      #returns consecutive sine waves