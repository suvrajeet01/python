#nested loop 3
#program for bulk reservation system by using a for loop inside while loop

travel = input('Yes OR No ')
while travel == 'yes':
    num = int(input('Number of people travelling : '))
    for num in range(1,num+1):
        name = input('Name: ')
        age = int(input('Age: '))
        sex = input('Male OR Female: ')

        print(name)
        print(age)
        print(sex)
    travel = input('Forgot someone? ')
