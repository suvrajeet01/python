
def func():
    print('first function')
    def funct2():
        print('first child function')
    def funct3():
        print('second child function')
    funct2()
    funct3()
func()