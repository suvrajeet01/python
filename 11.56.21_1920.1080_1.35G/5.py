#collections in python
    #collections are container data types which are used to store collections of data
    #4 collection data types
        #python general purpose collection data types
        #lists -declared in square brackets [];immutable(values can be changed);can store duplicate values;can be accessed using index
        #tuples - ordered and immutable(values can't be changed once declared) in nature;can hold duplicate entries
        #sets - unordered;declared on {};not indexed(elemens inside can't be accessed using indexes);doesmot hold duplicate values
        #dictionary - has key:value pairs;immutable(valuse can be changed);declared using {}

#module name - collection (with specialised data structures)
#collection module = collections ->specialised collection data structures
#specialised collections data types
    #1.namedtuple()
    #2.chainmap
    #3.deque
    #4.counter
    #5.ordereddict
    #6.defaultdict
    #7.userdict
    #8.userlist
    #9.userstring

#namedtuple() - returns a tuple with named value for each element in tuple
from collections import namedtuple
#make = (name = 'yu' , model = 'yureka' , model1 = 'yutopia')
a = namedtuple('manufacturer','name , model')
b = a ('Xiaomi','Black Shark 2 Pro')
print(b)
#implementing tuple using list i.e. fetching the values of namedtuple using list
a = namedtuple('manufacturer','name , model')
c = a._make(['Asus','Rog Phone 2'])
print(c)
#named entries can be obtained for the values inside the tuple

#deque - optimised list to perform insertions and deletions easily
#Deque(['g','a','m','e','r'])
from collections import deque
d = (['g','a','m','e','r'])
print(deque(d))
#OR
e = deque(d)
print(e)
#operations that can be performed on deque
e.append('of republic')     #append - adding value at the end(of the deque)
print(e)
e.appendleft('republic of') #appendleft - adding value at the begining
print(e)
e.pop()                     #pop() removes the value that is at the top of the stack i.e. the value at the end
print(e)
e.popleft()                 #popleft() removes the value from the begining of the string
print(e)
#optimised version of insertion and deletion using deque

#chainmap - dictionary like class that can make OR is able to create single view of multiple mappings
#basically returns a list of several other dictionaries
from collections import ChainMap
d1={1:'asus',2:'rog phone 2'}
d2={3:'Xiaomi',4:'black shark 2 pro'}
d12=ChainMap(d1,d2)
print(d12)                  #chainmap-single view for multiple mappings


#counter - a dictionary subclass used to count hashable objects
#hashable objects -iterable objects likelist,tuples,set
    #a=[1,2,3,4,2,3,4,5,3,2,2,2,2,4,6,7,33,0]
    #count=counter(a)
    #counter({1:1,2:6,... and so on})
from collections import Counter
c1 = [1,2,3,4,2,3,4,5,3,2,2,2,2,4,6,7,33,0]
c2 = Counter(c1)
print(c2)                   #prints out the no. of times a number has occured in the list
#functions in counter
print(list(c2.elements()))  #elements function returns a list with all the elements inside the counter
print(c2.most_common())     #most_common function return a sorted list with count of each element inside the counter
sub={2:1,3:2}               #subtract function removes one 2 and two 3s from the list
print(c2.subtract(sub))
print(c2.most_common())

#ordereddict - a dictionary subclass that remembers the order in which the entries were added to the dictionary
#even if the value of the key is changed the position will not be changed because of the order in which it was inserted to the dictionary
from collections import OrderedDict
od=OrderedDict()
od[1] = 'p'
od[2] = 'y'
od[3] = 't'
od[4] = 'h'
od[5] = 'o'
od[6] = 'n'
print(od)               #prints out the character with respect to position(key) or index value
#functions in ordereddict - much similar to that of dictionary
print(od.keys())        #prints out the keys out of the key-value pairs of the dictionary
print(od.items())       #prints out key:value pairs of the dictionary
print(od)
od[1]='j'               #replacing the values
print(od)               #since the insertion was made at begining the value remains the same as it remembered the order in which the elements were added

#defaultdict - a dictionary subclass that calls a factory function to fill or supply missing values and doesnot throw any error when a missing key:value is called in the dictionary
    #D=defaultdict(int)
    #D['rog phone 2'] = 1
    #D['black shark 2 pro] = 2
    #print(D['red magic 3])
from collections import defaultdict
dd=defaultdict(int)
dd[1] = 'rog phone 2'
dd[2] = 'black shark 2 pro'
print(dd)
print(dd[3])

#case with normal dictionary
dic={
    1 :'rog phone 2',
    2 :'black shark 2 pro'
}
print(dic)
#print(dic[3])          //key error is obtained since 3 is not present or defined inside a ordinary dictionary
#but defaultdict doesnot throw a key error even if the value is missing inside the dictionary

#userdict - wrapper around dictionary objects for easier dictionary sub-classing
    #it's need arose from the necessity to subclass directly from the dictionary as the  underlying dictionary becomes an attribute
#userlist - wrapper around list objects for easier list sub-classing
    #useful base class for other classes that can inherit from them and overwrite the existing methods or add a new one as well
    #it's need came from the necessity to subclass directly from list and is easier to work with this class as the undderlying list becomes an attribute as well
#userstring - wrapper around string objects for easier string sub-classing
    #the nees for this class is partially sub-planted by the ability to sub class direcly from strings
    #easier to work with as underlying string is accessible as an attribute
