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