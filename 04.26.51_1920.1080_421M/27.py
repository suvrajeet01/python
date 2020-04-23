#try except
#catching errors in python
#try except blocks to reduce the chances of error
#if a user enters a string inplace of a number the interpreter throws an error
#to solve this kind of problems except blocks tries out a piece of code and if it encounters a error then it shows warning instead of error

try:
    a = 10/0
except ZeroDivisionError as err:        #storing ZeroDivisionError in a variable named err
    print(err)
try:
    number = int(input('enter a number: '))
    print(number)
except ValueError:                      #errors must be named in except blocks as it is a good practise
    print('invalid input')