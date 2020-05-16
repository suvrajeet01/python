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