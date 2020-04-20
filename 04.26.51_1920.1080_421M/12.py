#List functions - functions in list

lucky_numbers = [4,8,15,16,7,2]
friends = ['kevin' , 'george' , 'edward' , 'oscar' ,'tobby']
friends.extend(lucky_numbers)   #.extend() functions is used to append one list onto end of another list
print(friends)
friends.append('Kassandra')        #.append() function allows to add items to the end of the list
friends.append('Alexios')          #.append() function add items at the end and takes only one argument
friends.insert(1, 'Theranos')       #.insert function is used to add items by specifying index number
print(friends)
friends.remove('oscar')             #.remove function is used to delete OR remove items from the list
print(friends)  
friends.clear()                     #.clear() removes OR gets rid of all the items from the list 
print(friends)
friends1 = ['kevin','edward' , 'george' , 'edward' , 'oscar' ,'edward' ,'tobby']
friends1.pop()                       #pops out OR removes the last item from the list
print(friends1)
print(friends1.pop())
print(friends1.index('george'))      #.index('value') specifies out the index number of the value OR item in the list
print(friends1.count('edward'))      #.count() function counts the total number of occurence of the value specified in the parameter of the count function
friends2 = ['kevin' , 'george' , 'edward' , 'oscar' ,'tobby']
friends2.sort()             #.sort() function sorts the list in ascending order in this case alphabetically
print(friends2)
print(friends2.sort())      #gives out result as none?
lucky_numbers.sort()        #sorts the list in ascending order
print(lucky_numbers)
lucky_numbers.reverse()     #reverses the list
print(lucky_numbers)
friends3 = friends2.copy()  #copies the content of one list to another
print(friends3)
