#decorators continued
def function1(function):
    def wrapper(*args,**kwargs):
        print('python')
    return wrapper
@function1
def function2(name):
    print(f'{name}')
function2('java')