#operators in python

#arithmetic - used to perform arithmetic operations between variables;they include -> +,-,*,/
a = 10
b = 20
print(a+b)
print(a-b)
print(abs(a-b))
print(a/b)
print(a*b)
print(a**b)         #**(exponentiation)
print(a%b)          #%(modulus)
print(a//b)         #//(floor division)
print(b//a)
#assignment - are used to assign values
#they include =,+=,-=,*=,%=,**=,//=,|=,^=,&=
c = 20
c+=5
c**=5
print(c)
#comparison - used  to compare two values or objects
#they include(==,!=,>,<,<=,>=)
c1 = 10
c2 = 20
c3 = c1 == c2
print(c3)
print(c1 == c2)
c3 = c1 > c2
print(c3)
print(c1 < c2)
#logical -used to combine condition statements
 #conditional statements(three types)
l1 = 10
l2 = 10

if l1 == l2:        #if statement
    print('equal')
elif c2 > c1:       #elif(elseif) statement
    print('greater')
else:               #else statement
    print('smaller')

if l1 != l2:
    print('equal')
elif c2 > c1:
    print('greater')
else:
    print('smaller')
#will only proceed to next statement ifthe first condition is false
if l1 != l2:
    print('equal')
elif c2 < c1:
    print('greater')
else:
    print('smaller')

if l1 != l2:
    print('equal')
elif c2 < c1:
    print('greater')
else:
    print('smaller')

 #logical operators - and;or;not
lo1 = 76
print(lo1 > 32 and lo1 < 56)        #and ->both the conditions are required to be in same state(either true or false) to obtain true
print(lo1 > 32 or lo1 < 56)         #or ->any one of the value need to be true to get the result as true and vice-versa
print(not(lo1 > 32 and lo1 < 56))   #not ->negates the statement given as parameter i.e. converts true to false and vice-versa and finally the opposite value is obtained

#identity - used to compare objects
list1 = [10,20,30]
list2 = [10 , 20 , 30]
    #is - returns true if both variables are same object
i1 = list1
print(i1 is list1)
print(list1 is list2)       #values are same but are different objects
print(list1 == list2)
    #is not - returns true if both variables are not same object
print(list1 is not list2)

#membership - used to check the presence of sequence in an object
    #in - returns true if a sequence with the specified value is present in the object
print(i1 in list1)
print(list1 in list2)       #values are same
print(10 in list1)
print([10 , 20 , 30] in list2)

    #not in - returns true if a sequence with the specified value is not present in the object
print(list1 not in list2)

#bitwise - used to compare binary values or numbers
#they include :-
print(10 & 12)  # &(bitwise and) - sets each bit to 1 if both bits are 1
print(10 | 12)  # |(bitwise or) - sets each bit to 1 if one of the bits is 1
print(10 ^ 12)  # ^(bitwise xor) - sets each bit to 1 if only one of the bit is 1
print(~10)      # ~(bitwise not) - inverts all bits
print(10 << 2)  # <<(left shift) - shift left by pushing in zeroes from right and let the leftmost bits fell off
print(10 >> 2)# >>(right shift) - shift right by pushing copies of leftmost bits in from left and let the rightmost bit fall off
