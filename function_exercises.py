'''
Basic exercises in writing functions
'''
from math import sin
import matplotlib.pyplot as plot
from numpy import arange


# 1) Write a function f(x) that returns x + 1 and plot it for x values of -3 to
#    3 in increments of 1

def plot_values(user_min, user_max):
    '''
    returns x + 1 coordinates for range of Xs
    '''
    x_coords = range(user_min, user_max + 1)
    y_coords = []
    for coord in x_coords:
        y_coords.append(coord + 1)
    return x_coords, y_coords

# 2) Weite a function f(x) that returns x squared and plot its values
def plot_square_values(user_min, user_max):
    '''
    Returns x ** x coordinates for range of Xs
    '''
    x_coords = range(user_min, user_max + 1)
    y_coords = []
    for coord in x_coords:
        y_coords.append(coord ** 2)
    return x_coords, y_coords

# 3) Write a function f(x) that returns 1 if x is odd and -1 if x is even. Plot
#    it for x values of -5 to 5 in increments of 1.
def plot_even_or_odd(user_min, user_max):
    '''
    For a given set of x inputs, evaluates wheter each input is even or odd.
    Evaluates to -1 for even and 1 for odd. Returns two lists.
    '''
    x_coords = range(user_min, user_max + 1)
    y_coords = []
    for coord in x_coords:
        if coord % 2 == 0:
            y_coords.append(-1)
        else:
            y_coords.append(1)
    return x_coords, y_coords

# 4) Write a function f(x) that returns the sin of x
def plot_sin_values(user_min, user_max):
    '''
    For a given set of x min and max inputs, creates a list of x-coords that
    cooresponds to the range of the inputs, and a second list that gives the
    corresponding sin values
    '''
    x_coords = range(user_min, user_max + 1)
    y_coords = []
    for coord in x_coords:
        y_coords.append(sin(coord))
    return x_coords, y_coords

# 5) Write a function f(x) that returns the sin of x in .1 increments
def plot_sin_values_hires(user_min, user_max):
    '''
    For a given set of x min and max inputs, creates a list of x-coords that
    cooresponds to the range of the inputs, and a second list that gives the
    corresponding sin values. Resolution is .1
    '''
    x_coords = arange(user_min, user_max + .1, .1)
    y_coords = []
    for coord in x_coords:
        y_coords.append(sin(coord))
    return x_coords, y_coords

# 6) Write a function that takes a temperature in Celcius and converts it
#    to Fahrenheit
def celsius_to_fahrenheit(user_min, user_max):
    '''
    Converts a range of cel. temps to fht. temps, from user min to user max
    (inclusive).
    '''
    celsius_temps = range(user_min, user_max + 1)
    fahrenheit_temps = []
    for deg in celsius_temps:
        fahrenheit_temps.append(deg * 1.8 + 32)
    return celsius_temps, fahrenheit_temps

# 7) Write a function that prompts the user for input, asking them "Do you want
#    to play again (Y on N)?". If the user answers "Y", the function should
#    return True, otherwise, it should return False.
def play_again():
    '''
    Asks the user if they want to keep playing. Returns True or False.
    '''
    keep_playing = raw_input("Would you like to keep playing? (Y / N)> ")
    if keep_playing.upper() in ['YES', 'Y', 'SURE', 'DEFINITELY']:
        return True
    return False

# 8) Write a function that asks the user whether they want to play again like
#    the previous problem. Except this time, they have to answer with either
#    "Y" or "N", if they give an invalid input, it should say "Invalid input."
#    and prompt the user again for an answer. When the user finally gives a
#    valid input, the function will return True if it was "Y", and False if it #    was "N".
def play_again_validation():
    '''
    Asks the player if they want to play again. Enforces input to help resolve.
    '''
    keep_playing = raw_input("Would you like to keep playing? (Y / N)> ")
    while keep_playing.upper() not in ['Y', 'N']:
        keep_playing = raw_input('''I\'m sorry, that\'s not a valid answer.
        Please answer with a \'Y\' or \'N.\'> ''')
    if keep_playing == 'Y':
        return True
    return False

# Test all the functions!
def test():
    # pylint: disable-msg=R0914
    # ^ disabling pylint local variable refactor warnings for this method
    # since we're just passing some valid params as tests
    '''
    calls all the other functions in this module as a simple output test
    '''
    # test for plot_values()
    x_min = -3
    x_max = 3
    x_range, y_range = plot_values(x_min, x_max)
    plot.plot(x_range, y_range)
    plot.show()

    # test for plot_square_values()
    x_squared_min = -100
    x_squared_max = 100
    x_squared_range, y_squared_range = plot_square_values(x_squared_min,
                                                          x_squared_max)
    plot.plot(x_squared_range, y_squared_range)
    plot.show()

    # test for even / odd:
    x_even_odd_min = -5
    x_even_odd_max = 5
    x_even_odd_range, y_even_odd_range = plot_even_or_odd(x_even_odd_min,
                                                          x_even_odd_max)
    plot.bar(x_even_odd_range, y_even_odd_range)
    plot.show()

    # test for sin plot
    x_sin_min = -5
    x_sin_max = 5
    x_sin_range, y_sin_range = plot_sin_values(x_sin_min, x_sin_max)
    plot.plot(x_sin_range, y_sin_range)
    plot.show()

    # test sin values hi res plot
    x_sin_hr_min = -5
    x_sin_hr_max = 5
    x_sin_hr_range, y_sin_hr_range = plot_sin_values_hires(x_sin_hr_min,
                                                           x_sin_hr_max)
    plot.plot(x_sin_hr_range, y_sin_hr_range)
    plot.show()

    # test degree unit conversion
    celsius_min = -100
    celsius_max = 100
    celsius_range, fahrenheit_range = celsius_to_fahrenheit(celsius_min,
                                                            celsius_max)
    plot.plot(celsius_range, fahrenheit_range)
    plot.show()

    # test keep playing
    print play_again()

    # test keep playing with validation
    print play_again_validation()

if __name__ == "__main__":
    test()
