#writing and appending to files
#python allows to work with external files be it read or write

employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()
#appending to a file
#each and every time the program runs the text gets appended to the file
employee_file = open("employees.txt", "a")  #a means append meaning adding text/content to the end of the file
employee_file.write('\nTobby - Human Resources')
employee_file.write('\nKate - Customer Service')
employee_file.write('\nTom - Manager')
employee_file.close()
#writing to a file
employee_file = open("employees1.txt", "w")      #w replaces everything;can be used to create a new file
employee_file.write('John - Senior Manager')
employee_file.close()
file1=open('index.html','w')
file1.write('<p>This is a HTML page</p>')
file1.close()
#using w OR write
    #existing files can be overwritten
    #write to a new file OR create a new file
    #append to the end of the file