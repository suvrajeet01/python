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
                        #accessing a series of letter from a string
                        #variable[starting index:ending index]
print(xs[1:9])
print(xs[1:13])
print(xs.upper())               #changes all letters from lowercase to uppercase
xs1 = 'UPPER CASE LETTERS'
print(xs1.lower())              #changes all letters of a a string from uppercase to lowercase
print(xs[-5])                   #accessing the value of a string from end
print(xs[6])

#________________________________________________________________________________________________________________________________________________        
    #list - collection of arrays that can be changed and are ordered ; they have indexes ; to declare [] are used ; different data types can be included in a same list together

fruits = ['apple', 'banana', 'grapes', 'orange']
print(fruits)
list = [10,20,30,2,30,10,'python','programming']
print(list)
print(list[2:5])                        #accessing the values using index number
print(list[1:100])
print([list])
list[2] = 1000                     #updating values in the list using index number
print(list)
list.append(3000)                  #adding values to list using append - append adds the value at the end of the list
list.append("iron.man")
print(list)
list.insert(5, 210)                    #adding values to the list using index number at any location - insert()function ; index(index, value)
print(list)
list1 = list

print(list1.reverse)                   #reversing the list using reverse function
print(list1)

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


    #tuple
    #set
    #range - for iterating through values