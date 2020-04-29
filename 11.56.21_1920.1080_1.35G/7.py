#hash table and hashmap are implemented using built-in dictionary data type in python
#hash table or a hashmap is a type of data structure that maps keys to its value pairs by implementing abstract data type
#hash table stores a key-value pairs and the key is generated using a hash function
#the keys of a dictionary are generated using a hashing function and the elements are unordered and can be changed

#creating dictonaries in python
#using {}
d1 = {'John' : '001','Bruce' : '002','Tony':'003'}
print(d1)
print(type(d1))

#using dict() function
d2 = dict()         #empty dictionary as no key:vaue pairs present
print(d2)
print(type(d2))

d2 = dict(John='001',Tony='002')
print(d2)

#nested dictionaries - dictionaries that lie within other diictionaries
nd1 = {'Employee':{'John':{'ID':'001','Salary':'2000000','Designation':'Team Leader'},
                    'Bruce':{'ID':'002','Salary':'3000000','Designation':'Agent'}}}
print(nd1)

#performing operations on hash tables
#accessing items
 #1.by using key value pairs
print(d1['John'])
print(d1)
 #2.using functions
print(d1.keys())
print(d1.values())
print(d1.get('Tony'))
 #3implementing for loop
for x1 in d1:               #for the values
    print(x1)
for x1 in d1.values():      #for the keys
    print(x1)
for x1,y1 in d1.items():    #using items() function
    print(x1,y1)

#updating values - dictionaries are mutable and values can be updated when required
d1['John'] = '004'
d1['Dave'] = '005'
print(d1)
#deleting entries
 #using functions
d1.pop('John')      #removes the item specified
print(d1)
print(d1.popitem()) #removes as well as returns the function
del d1['Bruce']      #del function removes the value given as parameter
print(d1)


#converting a dictionary to a dataframe
#dataframe - 2-D data structure that consists of columns of vvarious type;similar to python dictionary and it can be converted into a pandas dataframe
#import pandas as pd
#df = pd.DataFrame(nd1['Employee'])
#print(df)
#jupyter notebook