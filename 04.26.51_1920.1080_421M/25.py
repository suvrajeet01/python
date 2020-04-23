#building a basic translator
    #la lang
    #vowels -> l
    #--------------

    #dog ->dlg
    #cat ->clt

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + 'l'
        else:
            translation = translation + letter
    return translation

print(translate(input('enter a phrase: ')))

#OR

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + 'L'
            else:
                translation = translation + 'l'
        else:
            translation = translation + letter
    return translation

print(translate(input('enter a phrase: ')))