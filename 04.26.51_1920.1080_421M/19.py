#dictionaries - special structure in python that allows to store information in key value pairs
#keys must be unique ; values may be duplicate
#program to convert three digit month name to full name
#used to store different types of data
monthConversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December',
}

#accesing vales of a dictionary
print(monthConversions['Nov'])
print(monthConversions['Mar'])

#alternate method to get the value
print(monthConversions.get('Dec'))      #get() function is used to specify the default value if the given key is not found
print(monthConversions.get('man'))      #here if the .get() function would not have been used instead of getting none it would have been resulted with an error
print(monthConversions.get('man', 'not a valid key'))       #passing a dafault value if the key is not found in the dictionary

#kay may be number , not necessary to be a string or anything as long as they are unique

monthConversions1 = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}