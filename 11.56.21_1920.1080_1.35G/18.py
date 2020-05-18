#decorators continued

#decorator with arguments
def function1(function):
    def wrapper(*args,**kwargs):        #arguments inside a wrapper function
        print('Hello')
        function(*args,**kwargs)
        print('welcome to Python world')
    return wrapper
@function1
def function2(name):
    print(f'{name}')

function2(input('Enter you name: '))

#return values from a decorated function

def function11(function):
    def wrapper1(*args, **kwargs):
        print('It works')
    return wrapper1

@function11     #syntactic sugar
def function22(name):
    print(f"{name}")

function22('python')