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

#hourglass pattern

def pattern(n):
    k = n - 2
    for i in range(n,-1,-1):                #the third parameter is step or the points to be skipped between each points from initial to final position
        for j in range(k,0,-1):
            print(end=' ')
        k +=1
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
    k = 2 * n - 2              #bs- blank spaces variable
    for i in range(0,n+1):        #loop for outer rows
        for j in range(0,k):   #loop for columns
            print(end = ' ')
        k = k - 1             #decrementing spaces
        for j in range(0,i+1):
            print('* ', end='')
        print('\r')
pattern(int(input('Enter a number')))

#half pyramid pattern
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
pattern(int(input('Enter a number')))

#left half pyramid pattern
def pattern(n):
    k=2*n -2
    for i in range(0,n):
        for j in range(0,k):
            print(end = ' ')
        k = k-2
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
pattern(int(input('Enter a number')))

#downward half pyramid
def pattern(n):
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print('* ', end='')
        print('\r')
pattern(int(input('Enter a number')))

#left downward half pyramid

#diamond pattern
def pattern(n):
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end = ' ')
        k = k - 1
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
    k = n - 2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end = ' ')
        k = k+1
        for j in range(0,i+1):
            print('* ',end = '')
        print('\r')
pattern(int(input('Enter a number')))

#diamond star pattern
for i in range(5):
    for j in range(5):
        if i+j==2 or i-j == 2 or i+j == 6 or j-i==2:
            print('*',end='')
        else:
            print(end=' ')
    print()

#number patterns
def pattern(n):
    x=0
    for i in range(0,n):
        x +=1
        for j in range(0,i+1):
            print(x,end=' ')
        print('\r')
pattern(int(input('Enter a number')))

#pascal's triangle
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(function(i,j),' ',end='')
        print()

def function(n,k):
    res = 1
    if(k>n-k):
        k=n-k
    for i in range(0,k):
        res = res * (n-i)
        res=res//(i+1)
    return res
pattern(int(input('Enter a number')))

#half pyramid pattern with numbers
def pattern(n):
    x=0
    for i in range(0,n):
        x = x +1
        for j in range(0,i+1):
            print(x,end=' ')
        print('\r')
pattern(int(input('Enter a number')))

#diamond pattern with numbers
def pattern(n):
    k = 2 * n - 2
    x = 0
    for i in range(0,n):
        x = x + 1 
        for j in range(0,k):
            print(end = ' ')
        k = k - 1
        for j in range(0,i+1):
            print(x,end=' ')
        print('\r')
    k = n - 2
    x = 0
    for i in range(n,-1,-1):
        x = x +1
        for j in range(k,0,-1):
            print(end = ' ')
        k = k+1
        for j in range(0,i+1):
            print(x,end = ' ')
        print('\r')
pattern(int(input('Enter a number')))

#descending order pattern(also a downward half pyramid pattern)
def pattern(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end='')
        print('\r')
pattern(int(input('Enter a number')))

#binary number pattern program(pyramid pattern with binary number)
def pattern(n):
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=' ')
        k = k-1
        for j in range(0,i+1):
            print('10',end='')
        print('\r')
pattern(int(input('Enter a number')))

#character pattern program
#right alphabetical triangle
def pattern(n):
    x=65        #ascii value is taken;65 for A  
    for i in range(0,n):
        ch = chr(x)     #changing to character vawriable
        x = x +1
        for j in range(0,i+1):
            print(ch,end= ' ')
        print('\r')
pattern(int(input('Enter a number')))

#charater pyramid program
def pattern(n):
    k = 2*n -2
    x = 65
    for i in range(0,n):
        for j in range(0,k):
            print(end = ' ')
        k = k - 1
        for j in range(0,i+1):
            ch = chr(x)
            print(ch,end = ' ')
            x = x+1
        print('\r')
pattern(int(input('Enter a number')))