'''
Methods that utilize the turtle graphics library to draw geometric shapes
from triangles to octagons. Also includes method for pentagram stars.
PY101 assignments...
'''
import turtle
# pylint: disable=no-member
# ^ disable errors for turtle not having the below methods, as they're
#   created dynamically

# 1) Draw an equilateral triangle
def draw_equilateral(side):
    '''
    Draws an equilateral triangle of specified user side. Starts the first
    line at 30 deg right offset from current heading (starts at bottom left)
    '''
    # Initialize heading. Assume default absolute heading of 90 deg
    turtle.left(60)
    # Draw first line
    turtle.forward(side)
    # Turn and draw the remaining sides
    for _ in range(2, 4):
        # Turn to the next side
        turtle.right(120)
        #Draw the next side
        turtle.forward(side)

# 2) Draw a square
def draw_square(side):
    '''
    Draws a square onscreen with side length passed in as an arg. Starts at
    bottom left corner and assumes default absolute heading of 90 deg.
    '''
    #Initialize heading, assuming baseline heading of absolute 90 deg.
    turtle.left(90)
    # Draw first line
    turtle.forward(side)
    # Turn and draw the remaining sides
    for _ in range(2, 5):
        # Turn to the next side
        turtle.right(90)
        # Draw the next side
        turtle.forward(side)

# 3) Draw a pentagon
def draw_pentagon(side):
    '''
    Draws a pentagon, beginning at the bottom left corner of the shapes
    (assuming default absolute heading of 90 degrees). Takes side length as
    an argument.
    '''
    # Initialize heading
    turtle.left(108)
    # Draw first line
    turtle.forward(side)
    # Make a turn and draw each of the remaining sides
    for _ in range(2, 6):
    # Turn to the next side
        turtle.right(72)
        # Draw the next side line
        turtle.forward(side)

# 4) Draw a hexagon
def draw_hexagon(side):
    '''
    Draws a hexagon with side length passed in as arg. Starts at bottom left
    corner, assuming starting heading of absolute 90 degrees.
    '''
    # Initialize heading
    turtle.left(120)
    # Draw first side
    turtle.forward(side)
    # Make a turn and draw each of the remaining sides
    for _ in range(2, 7):
        # Turn to the next side
        turtle.right(60)
        # Draw the next side
        turtle.forward(side)

# 5) Draw an octagon
def draw_octagon(side):
    '''
    Draws an octagon with side length passed in as an arg. Starts at bottom
    left, assuming a starting heading of absolute 90 degrees.
    '''
    # Initialize heading
    turtle.left(135)
    # Draw first side
    turtle.forward(side)
    # Turn and draw the remaining sides
    for _ in range(2, 9):
        # Turn to second side
        turtle.right(45)
        # Draw second side
        turtle.forward(side)

# 6) Draw a star
def draw_star(side):
    '''
    Draws a pentagram star, with the farthest point-to-point distance
    specified with an arg. Starts at bottom-left point, assuming absolute
    starting heading of 90 deg.
    '''
    # Initialize heading
    turtle.left(72)
    # Draws first line
    turtle.forward(side)
    # Turns and draws the remaining sides
    for _ in range(2, 6):
        turtle.right(144)
        turtle.forward(side)

# 7) Draw a circle
#    We don't need a function for this, as turtle.circle() accomplishes the
#    the same and is callable externally through this module's turtle import
