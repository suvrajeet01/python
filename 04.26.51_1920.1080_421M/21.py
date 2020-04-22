#building basic a guessing game
#using variables,if statemments,while loops

secrectWord = 'giraffe'
guess = ""      #empty string
guessCount = 1
guessLimit = 4
OutOfGuess = False

while guess != secrectWord and not(OutOfGuess):
    if guessCount < guessLimit:
        print('Guess ' ,guessCount, ' of 3 ')
        guess = input('Enter guess: ')
        guessCount += 1
    else:
        OutOfGuess = True
if OutOfGuess:
    print('Out of guesses , YOU LOSE!')
else:
    print('You  win!')