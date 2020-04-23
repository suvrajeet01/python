#Reading files
#reading from external files in python
#python read command helps to read files that are outside python files
#functions used
    #.read()
    #.readline()
    #.readlines()
    #.readable()


employee_file = open("employees.txt", "r")  #0#1
print(employee_file.readable())     #2
print(employee_file.read())         #3
employee_file.close()               #5

print()

employee_file = open('employees.txt', 'r')
print(employee_file.readline())     #4
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()


employee_file = open('employees.txt', 'r')
print(employee_file.readlines())    #6
employee_file.close()
print()
employee_file = open('employees.txt', 'r')
print(employee_file.readlines()[1])    #7
employee_file.close()
print()
employee_file = open('employees.txt', 'r')
for employee in employee_file.readline():
    print(employee)
employee_file.close()
print()
employee_file = open('employees.txt', 'r')
for employee in employee_file.readlines():   #8
    print(employee)
employee_file.close()


#0opening file that is to be read
#1.open(filename with path, mode in which file has to opened) -> path may be relative(if in same folder or directory) or absolute(if in different folder or directory);modes -> r for read:only for viewing the file, w for write: for modifying OR changing the file,a for append : to append OR to only add information at the end of the file, r+ for read and write
#2.to check weather the file is readable or not
#3.displays all the information inside te file
#4.reading individual line from the file
#5.whenever a file is opened it is needed to be closed so that it is no longer accessible
#6.takes all the elements or each line of the file and prints it inside a array (list)
#7.reading or accessing a specific line it can be refered by using index in array
#8.using readlines function with a for loop -> will loop through all the lines in the file that prints out individual lines