#patterns in python
#types :-star pyramid;half pyramid;triangle pattern;hourglass pattern;diamond pattern;inverted pyramid patterns

#pyramid
def pattern(num):
    bsps = 2 * num - 2              #bs- blank spaces variable
    for i in range(0,num):        #loop for outer rows
        for j in range(0,bsps):   #loop for columns
            print(end = ' ')
        bsps = bsps - 1             #decrementing spaces
        for j in range(0,i+1):
            print('* ', end='')
        print('\n')

pattern(int(input('Enter a number')))

def pattern(n):
    bs = 2 * n - 2              #bs- blank spaces variable
    for i in range(0,n):        #loop for outer rows
        for j in range(0,bs):   #loop for columns
            print(end = ' ')
        bs = bs - 1             #decrementing spaces
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')

pattern(int(input('Enter a number')))

#inverse pyramid
def pattern(n):
    k = 2*n -2
    for i in range(n,-1,-1):            #the third parameter in range function specifies the number of spaces
        for j in range(k,0,-1):
            print(end=' ')
        k +=1
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
pattern(int(input('Enter a number')))

def pattern(n):
    k = n -2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=' ')
        k +=1
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
pattern(int(input('Enter a number')))

#right star pattern program
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
pattern(int(input('Enter a number')))

def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
    for i in range(n,0,-1):
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
pattern(int(input('Enter a number')))

#left star pattern
def pattern(n):
    k = 2 * n - 2
    for i in range(0,n-1):
        for j in range(0,k):
            print(end=' ')
        k -=2
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
    k -=1
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=' ')
        k +=2
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')

pattern(int(input('Enter a number')))