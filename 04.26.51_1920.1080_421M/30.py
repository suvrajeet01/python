#Modules and pip
#using modules in python
#modules are external python files that can be imported to current python file and all the functions and other stuffs from that file can be used in the current file after importing it

import useful_tools     #importing external python file or module
print(useful_tools.roll_dice(10))   #importing function from external file

#find list of all supported modules
    #goto google.com
    #list of pyython modules
    #click the docs website of the version using(3.8)
    #huge list of python modules can be found here that can be imported and used according to needs
    #third party modules can also be found outside of python docs
    #module for a specific purpose can also be found out there in google written by other developers or peoples out there
        #lot of useful and other modules may not be in module docs in python website or in lib folder in installation directory by default



#two types of modules
    #built-in modules - built in with the interpreter
    #external modules - are stored where python is installed in the system
        #stored inside lib folder where python is installed
        #the location of external modules can be found in modules docs
            #click on the desired module to know it's location if present in install directory of python




#installing python modules that are not pre-installed
    #find the module to be installed
        #ex:- google ->python-docx
        #goto python-docx website
        #follow the install instruction
        #can be installed using pip install python-docx



#pip(comes pre-installed with python 3 or later)
#it is a program used to install python modules(can be called as OR reffered to as a package manager)
#using pip user can
    #install , manage , update , remove(uninstall) different python modules
#installing using pip
    #open cmd for windows and terminal for mac/linux
    #pip --version to check weather pip is installed or not
    #to install a python module
        #pip install module-name
        #ex:- pip install python-docx
        #these modules are stored inside python(install directory)/lib/site-packages
        #to use the modules
            #import module-name
            #ex:-import docx
    #to remove a python module
        #pip uninstall python-module-name
        #ex:-pip uninstall python-docx



