#arrays - a data structure that can hold more tha one value at a time
        #collection OR ordered series of elements of the same type
        #all the values in an array have a particular address that is specified by its index number
        #indexing always starts from 0(zero)
        #length of array = n;index =n-1
    #difference between list and arrays
        #python arrays and list stores the data in same way
        #arrays can store only single data type value while list can store different data types
        #mathematical operations,looping,slicing,iterations can vary depending on the type of data stored in either of them
    #to create array a module named array has to be imported
    #3 types to import an array
        #import array
        #import array as arr
        #from array import * - imports all that is present in array module
import array
a = array.array('i',[1,2,3,4,5,6])      #array.array - name of module.array constructor ('type of value OR the data type it'll hold)
print(a)

import array as arr     #arr here is alias name
b=arr.array('i',[1,2,3,4,5,6])
print(b)

from array import *
c=arr.array('i',[1,2,3,4,5,6])
print(c)

#accessing array elements using index value
#negative indexing also exists
    #starts from right hand side and move towards left hand side
    #starts from -1;length of array=n;index of 1st element=-n;index of n element=-1
print(a[2])

#operations on array
print(len (a))                 #len()-length of array
print(len (b))
print(len (c))
                                #adding/changing element of array
a.append(7)                   #append() - adds single element at the end of the array
a.append(8)
print(a)
print(len(a))
b.extend([7,8,9])             #extend() - to add more than one element at the end of the array
print(b)
print(len(b))
c.insert(6,7)               #insert() - to add an element at a specific position in an array
                            #1st parameter is index value and 2nd parameter is the element to be added to that index position
print(c)
print(len(c))
                            #remove/delete elements from array
a.pop()                     #pop() - removes the element but returns it;takes idex value as parameter
print(a)
b.pop(-3)
print(b)
#remove() - removes an element with a specific value without returning it
#array concatenation
#slicing
#looping through an array