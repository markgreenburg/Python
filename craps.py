'''Simple craps game'''
from random import randint

def get_drink():
    '''Prints a welcome message, and asks for the user's drink of choice.'''
    print "Hi there! Welcome to the craps table."
    print "Would you like scotch or bourbon?"
    drink_of_choice = raw_input("> ").lower()
    while drink_of_choice != 'scotch' and drink_of_choice != 'bourbon':
        print "Sorry. That's not a drink we have. Please choose either scotch or bourbon."
        drink_of_choice = raw_input("> ").lower()
    print "Great! We'll get you some %s." % drink_of_choice
    print "..."
    print "Let's get started!"
    return drink_of_choice

def initialize_user_balance():
    '''Asks the user how much money they have, and validates that it's a real positive number'''
    balance_ok = False
    while not balance_ok:
        try:
            init_balance = int(raw_input("How much cash do you have in your stash?> ")) * 1.00
            if init_balance <= 0:
                init_balance = int(raw_input(
                    '''You need a positive balance to play...please
                    enter a positive balance>''')) * 1.00
            else:
                balance_ok = True
        except ValueError:
            init_balance = int(raw_input("I don't recognize that balance. Please enter number> "))
            initialize_user_balance()
    return init_balance

#def update_balance(initial_balance, won_or_lost):

def get_pass_bet(balance):
    '''Asks the user for a pass line bet and validates to positive int,
    less than remaining total balance.'''
    wager_ok = False
    while not wager_ok:
        try:
            bet = int(raw_input('''What would you like to wager on the pass
            line?> '''))
            if bet < 0:
                bet = int(raw_input(
                    '''You can't wager a negative number. What  kind of casino
                    do you think this is? Please wager a positive number.> '''
                    ))
            elif bet > balance:
                bet = int(raw_input(
                    '''We don't do loans here. Your wager can't be more
                    than your remaining balance ($%s).> ''' % balance
                    ))
            else:
                wager_ok = True
        except ValueError:
            bet = int(raw_input(
                '''I don't recognize that wager. Please wager a positive number
                no larger than your present balance ($%s).> ''' % balance
                ))
            get_pass_bet(balance)
    return bet
def roll_two_dice():
    '''Roles two six-sided dice on command'''
    raw_input("Press 'enter' or type your lucky phrase to roll the dice> ")
    roll_one = randint(1, 6)
    roll_two = randint(1, 6)
    return roll_one, roll_two

def set_point():
    '''Rolls dice and determines win, lose, or sets the point.
    Rolls until a point is set. Prints roll output. Returns value
    of each die, followed by total'''
    first_die_value, second_die_value = roll_two_dice()
    dice_total = first_die_value + second_die_value
    while dice_total in (2, 3, 7, 11, 12):
        if dice_total in (2, 3, 12):
            print "The come out roll was a %s. You lost! )-;" % dice_total

        else:
            print "The come-out roll was a %s. You won!" % dice_total
        first_die_value, second_die_value = roll_two_dice()
        dice_total = first_die_value + second_die_value
    print "Your roll was a %s. The point is set!" % dice_total
    return first_die_value, second_die_value

def play_again():
    '''Asks user if they want to play craps again & error checks their answer. Returns bool'''
    user_choice = raw_input("Would you like to play again? (y / n)> ").lower()
    acceptable_answers = ('y', 'yes', 'n', 'no')
    while user_choice not in acceptable_answers:
        user_choice = raw_input(
            '''Sorry, I didn't recognize that answer. Please answer yes or no and hit Enter> '''
            )
    if user_choice in ('y', 'yes'):
        return True
    return False

def roll_until_turn_end():
    '''Will roll the dice until the player wins or loses. Returns
    win or lose outcome of game as bool and prints message to user'''
    die_one, die_two = set_point()     #sets the point no matter what the roll
    point_on = die_one + die_two       #keep track of the point
    keep_rolling = True                #point is set so we need to keep rolling
    while keep_rolling:                #let's keep rolling until we win / lose
        die_one, die_two = roll_two_dice()  #here's the roll
        die_total = die_one + die_two  #add the dice up from the last roll
        if die_total == 7:             #if lost
            print "Sorry, your roll was %s. You lost!" % die_total
            keep_rolling = False
            user_won = False
        elif die_total == point_on:    #if won
            print "Woohoo, your roll was %s. You won!" % die_total
            keep_rolling = False
            user_won = True
        else:                          #if not lost or won, keep rolling
            print "You rolled %s. Please roll again." % die_total
    return user_won

def play_craps():
    '''Plays craps until the user doesn't want to play anymore'''
    user_drink = get_drink() #prints welcome msg, gets user's drink
    print "user drink is %s" % user_drink
    user_balance = initialize_user_balance() #set user starting balance
    print "user balance is $%s" % user_balance
    pass_bet = get_pass_bet(user_balance) #sets the uer's wager for the round
    print "user bets $%s" % pass_bet
    outcome = roll_until_turn_end() #keeps rolling until there's a w or l
    play_another_game = play_again()
    while play_another_game:
        outcome = roll_until_turn_end()
        play_another_game = play_again()
    print "Thanks for playing! See you later."
    return outcome

#Print some welcome messages and ask for the user's drink.

#sets the point and rolls until an outcome.
play_craps()
