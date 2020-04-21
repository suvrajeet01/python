#FUNCTIONS - are a block or collection of code that performs a specific opearation on execution
#def is used to define a function

def say_hi():
    print('Hello User')    #only the indented part after function declaration is considered to be function

#the code inside a function will only get executed when it is called (calling a function) i.e will not get executed automatically by default
say_hi()

#naming scheme for function
    #the name of the function must be in lowercase
    #for combinig 2 or more words '_'must be used
    #functions may take additional information that gets passed in are called as parameters
    #more than 1 parameter can be included
    #integer,strings,numbers,booleans,arrays and any other type of data can be passed as a parameter

def say_hi1(name, age):
    print('Hello ' , name , ', you are' , age)
    print('Hello ' , name , ', you are ' + age)

say_hi1('Mike', '56')
say_hi1('Steve', '34')

def say_hi2(name,age):
    print('Hello ' , name , ', you are ' + str(age))
say_hi2('Mike', 56)
say_hi2('Steve', 34)