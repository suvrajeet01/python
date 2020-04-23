#for loops in python
#for loop allows to loop over a different collections of items
    #i.e. looping through arrays,series of numbers or letters inside strings

for letter in 'python programming':     #defining a variable that changes on each iteration of the loop
    print(letter)                       #looping through all the letters og python programming string

friends = ['kevin','edward','george']        #array
print(len(friends))
for friend in friends:
    print(friend)
                                #name and friend are variables that for loop loops through
for name in friends:
    print(name)

for index in range(10):
    print(index)
                                    #the number in second position is not included in range
for index in range(3 ,10):
    print(index)
for index in range(len(friends)):       #another way to print elements in an array
    print(friends[index])

for index in range(5):
    if index == 0:
        print('first iteration')
    else:
        print('not first')