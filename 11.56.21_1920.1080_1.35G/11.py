#calculating factorial using for loop
num = int(input('Enter a number : '))
factorial = 1

if num < 0:
    print('must be positive')
elif  num == 0:
    print('factoial = 1')
else:
    for i in range(1,num+1):
        factorial = factorial * i
print(factorial)
