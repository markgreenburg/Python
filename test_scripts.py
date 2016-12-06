'''This is a basic guessing game. User can guess a random number between one
and 10, up to 5 tries. Script will notify if guess is too high or too low, and
prompt for another. Once the user either guesses correctly or runs out of
tries, we ask them if they'd like to play again, at which point we
re-initialize the guess counter and the random number'''

from random import randint

def guess_the_number(max_tries):
    '''Here we define the game as a function, with a max number of tries set by the user'''
    secret_number = randint(1, 10)
    print secret_number
    guess = 0
    tries = 0
    play_again = True

    while play_again:
        for _ in range(tries, max_tries):
            guess = int(raw_input("Guess a number between 1 and 10 > "))
            tries += 1
            if guess < secret_number:
                print "Sorry, %d is too low." % guess
            elif guess > secret_number:
                print "Sorry, %d is too high." % guess
            else:
                print "That's right! And it only took you %d tries!" % tries
                break
        else:
            print "Sorry, you're out of tries. The secret number was %d" % secret_number
        play_again = raw_input("Would you like to play again?> ")
        if play_again in ("Yes", "yes", "y", "Y"):
            play_again = True
            tries = 0
            secret_number = randint(1, 10)
            print secret_number
        else:
            play_again = False
