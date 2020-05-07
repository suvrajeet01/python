#decorators in python
#first class object - everthing including the data types and function as well are treated as an object.
#inner function - function defined inside a function


def func1(name):
    return f"Hello {name}"
def func2(name):
    return f"{name} , how you doin?"
def func3(func4):
    return func4("Dear one")

print(func3(func1))
print(func3(func2))


#using multiple functions insise a function
def func():
    print('first function')
    def funct2():
        print('first child function')
    def funct3():
        print('second child function')
    funct2()
    funct3()
func()

#some more s***
def fc(n):
    def fc1():
        return 'python'
    def fc2():
        return 'is OK'
    if n == 1:
        return fc1
    else:
        return fc2
a=fc(1)
b=fc(2)
print(a())
print(b())


#decorator modifies the behavior of the function without modifying its structure permanently and by wrapping another funtion and the callable function is returned as both the functions are callable.
#decorators are called before defintion of a function

def function1(function):
    def wrapper():
        print('hello')
        function()
        print('welcome to python')
    return wrapper
def function2():
    print('python')

function2=function1(function2)
