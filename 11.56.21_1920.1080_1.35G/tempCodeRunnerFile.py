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