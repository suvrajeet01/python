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
b=arr.array('i',[1,2,3,4,5,6])          #here i is the int data type
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
print(a.pop())                     #pop() - removes the element but returns it;takes index value as parameter
print(a)
print(b.pop(-3))                    #print statement returns the value removed by pop() function
print(b)
print(c)                    #remove() - removes an element with a specific value without returning it
print(c.remove(7))          #result/output is none i.e. remove() function doesnot return the value removed
print(c)

#array concatenation(joining) - possible only with same type of array
ac = arr.array('i',[1,2,3,4,5,6,7])
cc = arr.array('i',[6,5,4,3,2,1,0])
ca = arr.array('i')        #initializing empty array - specify the typecode and leave the valuelist empty
ca = ac + cc
print(ca)               #concatenation is not possible between two arrays with different data types;it will display type error - cannot concatenate arrays that hold different data type elements

#slicing - fetching values from array;done using ':' symbol(arrays can be sliced using : symbol, which in turn returns a range of elements specified by index numbers)
s = arr.array('i',[0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0])
print(s)
print(s[0:5])          #syntax - arr[initial position:final position];slicing returns the value that are between the range of initial and final position excluding the element at final position(i.e. the value at index final position will not be included)
print(s[0:-2])
sl = arr.array('i',[1,2,3,4,5,6,7,8,9])
print(sl[::-1])          #does not reverses the array but reprints out the reversed form of the array

#looping through an array
 #for loop - iterates over the item of an array specified number of times
fla = arr.array('i',[1,2,3,4,5,6,7,8,4,7,4,7,2,9,6,7,8,2])
print(fla)
for x in fla:
    print(x)
for x1 in fla[0:-3]:
    print(x1)
 #while loop - iterates over the element until a certain condition is met(or is true)
wla = fla
print(wla)
temp = 0                    #initializing iterator(temp)
while temp < wla[5]:        #specifying condition
    print(wla[temp])
    temp = temp+1           #OR temp+=1;incrementing iterator(if iterator is not incremented while loop will go on forever)
print(len(wla))

temp1 = 0
while temp1<len(wla):
    print(wla[temp1])
    temp1+=1
