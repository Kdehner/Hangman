import random
from bcolors import bcolor

dictonary = ['apple', 'banana', 'orange', 'mango', 'grape', 'watermelon', 'pineapple']
diccount = len(dictonary)
random = random.randrange(0,diccount)
word = list(dictonary[random])

gleft = 7
correct = ['_'] * len(word)
guessed = []
win = ''.join(word)

game = True

while True:
    print bcolor.BOLD + '-' * 25 + bcolor.ENDC
    print
    if gleft == 0:
        print bcolor.BOLD + bcolor.UNDERLINE + 'YOU LOSE!' + bcolor.ENDC
        print
        print "Your word was: ", ' '.join(word).upper()
        print
        quit()
    if correct == word:
        print bcolor.BOLD + bcolor.UNDERLINE + 'WINNER!' + bcolor.ENDC
        print
        print "Your word was: ", ' '.join(word).upper()
        print
        quit()
    print 'Welcome to Hangman. The word is going to be a fruit'
    print
    print ' '.join(correct).upper()
    print
    print 'Incorrect Guesses: ', ', '.join(guessed)
    print
    print 'You have: ', gleft, " incorrect guesses remaining!"
    print


    guess = raw_input('Guess a letter or word: ')

    if guess in word:
        if guess in correct:
            print bcolor.BOLD + bcolor.UNDERLINE + 'You already guessed that letter or word try again.' + bcolor.ENDC
            print
        else:
            print bcolor.BOLD + bcolor.UNDERLINE + 'CORRECT!' + bcolor.ENDC
            print
            position = [n for (n, e) in enumerate(word) if e == guess]
            i = 0
            while i < len(position):
                correct[position[i]] = guess
                i += 1
    else:
        if guess in guessed:
            if len(guess) <= 1:
                print bcolor.BOLD + bcolor.UNDERLINE + 'You already guessed that letter or word try again.' + bcolor.ENDC
                print

        else:
            print bcolor.BOLD + bcolor.UNDERLINE + 'INCORRECT!' + bcolor.ENDC
            print
            gleft -= 1
            guessed.append(guess)

    if guess == win:
        print bcolor.BOLD + bcolor.UNDERLINE + 'WINNER!' + bcolor.ENDC
        print
        print "Your word was: ", ' '.join(word).upper()
        print
        quit()
