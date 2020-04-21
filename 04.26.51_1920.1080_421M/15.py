#Return Statement
#using return statement in python functions
#return keyword allows the program to return information from a function
#after return keyword no new code can be added too the next line as the interpreter will skip it since return breaks back out of the function
#parameter is used to give information to the function and a return keyword is used to get information back from the function
#using return keyword any data type be it a string, array, boolean can be returned
def cube(num):
    return num*num*num

cube(4)
print(cube(4))
result = cube(4)
print(result)