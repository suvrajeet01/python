#building a better calculator in python that can perform all basic operations i.e. add, multiply, subtract and divide
#practical application of if statement

#whenever a input is taken from the user it gets converted to a string
num1 = float(input('enter first number: '))  #converting string to a number(float)
num2 = float(input('enter second number: '))
op = (input('enter operator either +/add ,-/subtract, */multiply, / OR divide :'))

if op == "+" or op == 'add':
    print(num1+num2)
elif op == '-' or op == 'subtract':
    print(abs(num1-num2))
elif op == '/' or op == 'divide':
    print(num1/num2)
elif op == '*' or op == 'multiply':
    print(num1*num2)
else:
    print('invalid operator')