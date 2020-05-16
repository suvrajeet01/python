#decorators in python
#first class object(also known as a function) - everthing including the data types and function as well are treated as an object.
#inner function - function defined inside a function

def func1(name):
    return f"Hello {name}"
def func2(name):
    return f"{name} , how you doin?"
def func3(func4):
    return func4("Dear one")

print(func3(func1))
print(func3(func2))

#using simplae decorator in python
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
#returning function from a function
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
    def wrapper():              #decorator here
        print('hello')
        function()
        print('welcome to python')
    return wrapper
def function2():
    print('python vs java')

function2=function1(function2)      #wrapper statement
function2()

#decorators using py syntax OR syntactic sugar
def function12(function121):
    def wrapper1():
        print('hello')
        function121()
        print('welcome to python')
    return wrapper1
@function12
def function21():
    print('python vs java')

function21()
