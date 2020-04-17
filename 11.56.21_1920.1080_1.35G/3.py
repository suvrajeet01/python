#variable data types
#six(+1) data types in python

    #number - numerical data type  
        #integer
x = 10
        #float
X = 10.234
        #complex
y = 25j     #j - imaginary part that is added to the number
        #boolean - returns only true or false value
            #used for only categorical output

a =101
b=10.25
c=10j
d=10>9

print(type(a)) 
print(type(b))
print(type(c))
print(type(d))

#_______________________________________________________________________________________________________________________________________________
    #string - written in single or double quotes in python
xs = 'hello world' 
                ##opearion on strings
print(len(xs))         #len - checks the lenngth of the string


##index numbers - starts from zero and counts on until the end of the string
#accesing value from a string usinng index number
print(xs[0])
print(xs[1])
print(xs[5])
                        #replacing values in string - strings are immutable i.e values can't be replaced or they cannot be changed
print(xs[1:9])                        #accessing a series of letter from a string
print(xs[1:13])                        #variable[starting index:ending index]


print(xs.upper())               #changes all letters from lowercase to uppercase
print(xs[0].upper(),xs[1:12])
xs1 = 'UPPER CASE LETTERS'
print(xs1.lower())              #changes all letters of a a string from uppercase to lowercase
print(xs[-5])                   #accessing the value of a string from end
print(xs[6])

#________________________________________________________________________________________________________________________________________________        
    #list - collection of arrays that can be changed and are ordered ; they have indexes ; to declare [] are used ; different data types can be included in a same list together

fruits = ['apple', 'banana', 'grapes', 'orange']
print(fruits)
list1 = [10,20,30,2,30,10,'python','programming']
print(list1)
print(list1[2:5])                        #accessing the values using index number
print(list1[1:100])
print([list1])
list1[2] = 1000                     #updating values in the list using index number
print(list1)
list1.append(3000)                  #adding values to list using append - append adds the value at the end of the list
list1.append("iron.man")
print(list1)
list1.insert(5, 210)                    #adding values to the list using index number at any location - insert()function ; index(index, value)
print(list1)
list11 = list1

print(list11.reverse)                   #reversing the list using reverse function
print(list11)

#________________________________________________________________________________________________________________________________________________

    #dictionary - collection of items just like list but unordered, changeable and indexed ; key : value pair are there, keys are indexes as are unique but values can be duplicaate
animals = {
        'reptiles' : 'snake',
        'mammals' : 'whale',
        'amphibians' : 'frogs',
}

courses = {
        1 : 'python',
        2 : 'data science',
        'third' : 'machine learning',
}
print(courses, animals)
print(courses[2])
print(courses['third'])
print(courses.get('third'))             #using  get() function to access the vale of dictionary
courses['third'] = 'hadoop'             #updating value of dictionary
print(courses)
courses['four'] = 'machine learning'    #adding new value or a new key value pair to dictionary
print(courses)

#________________________________________________________________________________________________________________________________________________

    #tuple - ordered and unchangeable (like strings) are held ; can contain duplicate entries

animals1 = (1,20,300,'lion',5000,'tiger',700,'monkey',80,'giraffe','tiger',1,300)
print(animals1)

print(animals1[2])              #tuples are indexed i.e index values can be used to access the items from the tuples
print(animals1.count(300))      #counting duplicate values using count function
print(animals1.count('tiger'))

#________________________________________________________________________________________________________________________________________________    
    #set - unordered / not indexed and cannot hold duplicate values
se = {10,20,30,30,40,10,50,2,0,20,'courses','animals','courses'}
print(se)
    #doesnot support indexing
#________________________________________________________________________________________________________________________________________________
    #range - for iterating through values
r=range(0,10)
print(r)

print(list(range(11))) #prints the vales of list i.e numbers from 0 to 11


#miscellaneous

a1=[1,2,3,4]        #list
b1={4,5,6,5,4}      #dictionary
c = [a1 , b1]       #list with list and dictionary
print(c)            #=> tuples and dictionaries can be embedded in a list
print([a1,b1])