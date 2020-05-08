def function1(function):
    def wrapper():
        print('hello')
        function()
        print('welcome to python')
    return wrapper
def function2():
    print('python')

function2=function1(function2)
function2()