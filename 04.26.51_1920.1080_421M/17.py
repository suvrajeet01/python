#comparing using comparisn operators using if statements
#using comparisns inside if statements
#comparisn operators include:
    #> -> greater than
    #< -> less than 
    #>= -> greater than and equal to
    #== -> equals
    #<= -> less than and equal to
    #!= -> not equal to
#comparisns can be done between nnumbers,booleans,strings,etc
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >=num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(3,4,5))
print(max_num(3,40,5))
print(max_num(300,40,5))