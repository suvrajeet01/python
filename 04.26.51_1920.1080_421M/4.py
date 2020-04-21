#functions - are a block or collection of code that performs a specific opearation on execution
#functions on string

phrase = "lion is the king of the jungle"
print(phrase)

print(phrase+'.')

print(phrase.lower()+'.')   # .lower() is a function that completely converts a string into lower case letters
print(phrase.upper()+'.')   # .upper() is a function that completely converts a string into uppper case letters

print(phrase.islower())   #.islower() function checks weather the given string is in lower case and returns a true or false value on the basis of that
print(phrase.isupper())   #.isupper() finction checks weather the given string is in upper case and returns a boolean value i.e either true or false on the basis of that
print(phrase.upper().isupper()) #functions can be used one after another..
print(len(phrase))      #len() function specifies the lenghth of the string
print(phrase[2])        #getting the character of a string using index number
print(phrase[0])        #prints out the first character of the string
print(phrase)
print('position with respect to index :-')
print('0123456789101112131415161718192021222324252627282930')
#in python string gets indexed from 0 OR ZERO

print(phrase.index('i'))       #.index() finction returns the index value of a character in a string when a character is given OR provided to the function
print(phrase.index('king'))

print(phrase.replace('jungle', 'woods.'))     #.replace("old string", "new string") function replaces characters or strings within string; it takes two parameters the string that is to be replaced i.e the old string and the new string after it