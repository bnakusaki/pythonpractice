import random

# A simple number guessing game

random_number = random.randint(0,21)
print('I\'m thinking of a number!\nTry to guess it')

while True:
    guess = int(input('I\'m thinking of...'))

    if guess<(random_number/2):
        print('Too low')
    elif (guess>=random_number/2) and (guess<random_number):
        print('Close, but Na!')
    elif guess>(random_number*2):
        print('Woah, that\'s too high!' )
    elif (guess>random_number) and (guess<random_number*2):
        print('you\'re guessing higher')
        
    else:
        print('Good guess🎊🎉')

    quit = input('Do you want to play again(Y/N)')
    if quit.lower == 'n':
        break


print(random_number)