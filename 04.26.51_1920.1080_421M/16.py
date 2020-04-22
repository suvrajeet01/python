#if statements in python
#used to make decissions
#i.e executes if the conditions required are met or fulfilled

is_male = True      #boolean variable
if is_male:
    print('You are a male')

#else keyword in python
#it's basically like otherwise
#if certain part of a if statement is false then the condition under else part is met

is_female = False
if is_female:
    print('you are a male')     #condition is false so is not printed out
else:
    print('you are not a male')

is_tall = True
#OR operator - #will execute if any one of the value is true
if is_male or is_tall:
    print('you are a male or tall or both')
else:
    print('you are neither male nor tall')


is_tall = False
is_male = False
if is_male or is_tall:
    print('you are a male or tall or both')
else:
    print('you are neither male nor tall')

#and operator - anly let the program execute if both the conditiona are true
is_tall = True
is_male = True
if is_male and is_tall:
    print('you are a tall male')
else:
    print('you are either not male or not tall or both')
#and will not execute if any of the conditions are false
is_tall = True
is_male = False
if is_male and is_tall:
    print('you are a tall male')
else:
    print('you are either not male or not tall or both')

#elif - stands for else if
#not function - negates whatever is inside the parenthesis i.e the parameters
    #i.e. if the parameter inside the not function is true it will make it false and vice versa
#1
is_male = True
is_tall = True
if is_male and is_tall:
    print('you are a tall male')
elif is_male and not(is_tall):
    print('you are a short male')
elif not(is_male) and is_tall:
    print('you are not a male but tall')
else:
    print('you are either not male and not tall')
#2
is_male = False
is_tall = True
if is_male and is_tall:
    print('you are a tall male')
elif is_male and not(is_tall):
    print('you are a short male')
elif not(is_male) and is_tall:
    print('you are not a male but tall')
else:
    print('you are either not male and not tall')
#3
is_male = True
is_tall = False
if is_male and is_tall:
    print('you are a tall male')
elif is_male and not(is_tall):
    print('you are a short male')
elif not(is_male) and is_tall:
    print('you are not a male but tall')
else:
    print('you are either not male and not tall')
#4
is_male = False
is_tall = False 
if is_male and is_tall:
    print('you are a tall male')
elif is_male and not(is_tall):
    print('you are a short male')
elif not(is_male) and is_tall:
    print('you are not a male but tall')
else:
    print('you are either not male and not tall')