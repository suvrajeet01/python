#lists in python
#lists helps to manage large amounts of data and organise it properly
#list is a structure that helps store information
#lists helps store multiple vales under a single variable
friends = ['kevin' , 'george' , 'edward' , 'oscar' ,'tobby']
print(friends)
#list starts indexing from 0 so the first element in the list will have index value 0
print(friends[0])
print(friends[2])
print(friends[-1])  #-ve number means indexing from back of the list
print(friends[-2])
print(friends[1:])  #grabs the item at index positon 1 with all the elements after it
#modifying items/values in lists
friends[3] = 'mike'
print(friends[3])