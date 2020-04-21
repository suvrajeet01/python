#Tuples - a type of data structure i.e. a container where different values can be stored
#tuples are immutable i.e they can neither be changed or modified
coordinates = (4,5)    #elements inside a tuples cannot be added or removed i.e. doesnot support item assignment
    #tuples supports index and like lists starts from 1
print(coordinates[0])

coordinates1 = [(4,5) , (6,7) , (80,34)]    #tuples inside list
print(coordinates1)
print(coordinates1[1])
coordinates1[1] =10
print(coordinates1)