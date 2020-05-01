#loops in python
#loops help to reduce size and length of the code;reduces the complexity;makes it more efficient and also increases the speed of execution

#loops allows execution of a statement or a group of statements multiple times
#in order to run a loop certain conditions are required to be true that are defined at the beginning of the loop
#and once the condition is false the loop stops and the control moves out of the loop
#pretest and post test loop
#in python only pretest loops present

#loops supported in python
#while loop - used when no. of iterations required are unknown and keeps iterating until a certain condition is met
ws = 0
while ws < 9:
    print('Number: ',ws)
    ws +=1
print ('exit loop')
#OR
ws = 0
we = 9
while ws < we:
    print('Number: ',ws)
    ws +=1
print ('exit loop')

#for loop - repeats a group of statements a specified number of times
#conditions/information/fields to be provided : boolean condition;initial or starting value of the counting variable;incrementation of the counting variable
fruits = ['mango','grapes','apple']
for fruit in fruits:
    print('current fruit: ',fruit)
print('exiting loop')
