#file handling
#CRUD - Create Read Update Delete
#python file hanndling system
    #create
    #open - open(filename,mode)
        #filename can be any file
        #mode - different modes for opening a file
            #r-for reading(default value);a-for append(either opens the file or creates it if it doesn't exist);w-opens file for writing(creates file if doesn't exist;overwrites the existing file);x-creates the specified file(returns error if file already exists)
            #additional parameters:- t-text mode(default value);b-binary mode(for images and other file types)
        #filename.read() - for reading the file
    #work
    #close


import os
file = open('1.txt','r')
print(file.read())  #reads out the content of the file
file.close()        #closes the opened file

file = open('1.txt','r')
print(file.read(5))     #reads out the first five characters of the file
file.close()

file = open('1.txt' , 'r')
print(file.readline())          #line by line output(firstline)
print(file.readline())          #second line
file.close()

file =open('1.txt' , 'r')
print(file.readline(3))         #read upto 3rd characters
file.close()

file =open('1.txt' , 'r')
print(file.readlines())         #read lines separately
file.close()


#looping over a file object - returning all the lines of a file in a efficient way
import os
file = open('1.txt','r')
for line in file:
    print(file.readlines())
file.close()

#writing to an existing file
file = open('demmo2.txt','w')
file.write('Hello World!')
file.write('\nSecond line')
file.close()

file = open('demmo2.txt','w')
file.write('oops overwritten!')
file.close()

#x - creates a file;returns error message if file exists
#a - append will either add content to the end of the file or will create a file if specified file doesnot exists
#w - will either create a file if the file doesn't exist or will overwrite the specified file


#file handling in python
#deletion operation - deleting the file
#os module must be imported
#os.remove() function is used 

import os
if os.path.exists('demmo2.txt'):
    os.remove('demmo2.txt')
    print('File deletion successful')
else:
    print('The file does not exist')