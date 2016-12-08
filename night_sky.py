'''
This script draws a night sky, using the turtle_graphics module
'''
import turtle
from random import randrange
import turtle_graphics

# pylint: disable=no-member
# ^ disable errors for turtle not having the below methods, as they're
#   created dynamically

def draw_star_layer(stars_to_draw, min_height, max_height, min_width,
                    max_width):
    '''
    Draws stars within the specified bounds of the screen at random. Star
    density, bounds, and size are passed in as args.
    '''
    for _ in range(stars_to_draw + 1):
        x_coord = randrange(min_width, max_width)
        y_coord = randrange(min_height, max_height)
        turtle.setposition(x_coord, y_coord)
        star_size = randrange(1, 10)
        turtle_graphics.draw_star(star_size, True, "White")

def initialize_night_sky(width, height, background_color):
    '''
    Initializes a canvas for the night sky drawing. Args are width, height
    and background color. Also speeds up drawing speed for convenience.
    '''
    # Specify the size of our canvas
    turtle.setup(width=width, height=height, startx=None, starty=None)
    # Set our background color per arg passed in
    night_sky_screen = turtle.getscreen()
    night_sky_screen.bgcolor(background_color)
    # Speed up our animation
    turtle.speed(10)


def draw_night_sky(background_color, stars_to_draw, width, height):
    '''
    Draws a night sky picture. Takes args to customize the picture.
    '''
    # Set the canvas size, background color, draw speed in one go
    initialize_night_sky(width, height, background_color)
    # Draw a layer of stars at random across top 2/3rds of the canvas
    draw_star_layer(stars_to_draw, - height * .2, height / 2, - width / 2, width / 2)
    # Don't clear drawing until keypress
    raw_input()


if __name__ == "__main__":
    draw_night_sky("black", 100, 960, 600)
