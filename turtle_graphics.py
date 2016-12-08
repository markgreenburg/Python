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
def draw_equilateral(side, fill_bool, color):
    '''
    Draws an equilateral triangle of specified user side. Starts the first
    line at 30 deg right offset from current heading (starts at bottom left)
    '''
    # Set fill vs. outline and color per args
    turtle.fill(fill_bool)
    turtle.color(color)
    # Initialize heading. Assume default absolute heading of 90 deg
    turtle.left(60)
    # Draw first line
    turtle.down()
    turtle.forward(side)
    # Turn and draw the remaining sides
    for _ in range(2, 4):
        # Turn to the next side
        turtle.right(120)
        #Draw the next side
        turtle.forward(side)
    # Reset turtle pen
    turtle.fill(False)
    turtle.up()

# 2) Draw a square
def draw_square(side, fill_bool, color):
    '''
    Draws a square onscreen with side length passed in as an arg. Starts at
    bottom left corner and assumes default absolute heading of 90 deg.
    Can be filled or outlined, with fill bool and color passed in as an arg.
    '''
    # Set fill vs. outline and color per args
    turtle.fill(fill_bool)
    turtle.color(color)
    #Initialize heading, assuming baseline heading of absolute 90 deg.
    turtle.left(90)
    # Draw first line
    turtle.down()
    turtle.forward(side)
    # Turn and draw the remaining sides
    for _ in range(2, 5):
        # Turn to the next side
        turtle.right(90)
        # Draw the next side
        turtle.forward(side)
    # Reset turtle pen
    turtle.fill(False)
    turtle.up()

# 3) Draw a pentagon
def draw_pentagon(side, fill_bool, color):
    '''
    Draws a pentagon, beginning at the bottom left corner of the shapes
    (assuming default absolute heading of 90 degrees). Takes side length as
    an argument. Can be filled or outlined, with fill bool and color passed in
    as an arg.
    '''
    # Set fill vs. outline and color per args
    turtle.fill(fill_bool)
    turtle.color(color)
    # Initialize heading
    turtle.left(108)
    # Draw first line
    turtle.down()
    turtle.forward(side)
    # Make a turn and draw each of the remaining sides
    for _ in range(2, 6):
    # Turn to the next side
        turtle.right(72)
        # Draw the next side line
        turtle.forward(side)
    # Reset turtle pen
    turtle.fill(False)
    turtle.up()

# 4) Draw a hexagon
def draw_hexagon(side, fill_bool, color):
    '''
    Draws a hexagon with side length passed in as arg. Starts at bottom left
    corner, assuming starting heading of absolute 90 degrees. Can be filled or
    outlined, with fill bool and color passed in as an arg.
    '''
    # Set fill vs. outline and color per args
    turtle.fill(fill_bool)
    turtle.color(color)
    # Initialize heading
    turtle.left(120)
    # Draw first side
    turtle.down()
    turtle.forward(side)
    # Make a turn and draw each of the remaining sides
    for _ in range(2, 7):
        # Turn to the next side
        turtle.right(60)
        # Draw the next side
        turtle.forward(side)
    # Reset turtle pen
    turtle.fill(False)
    turtle.up()

# 5) Draw an octagon
def draw_octagon(side, fill_bool, color):
    '''
    Draws an octagon with side length passed in as an arg. Starts at bottom
    left, assuming a starting heading of absolute 90 degrees. Can be filled or
    outlined, with fill bool and color passed in as an arg.
    '''
    # Set fill vs. outline and color per args
    turtle.fill(fill_bool)
    turtle.color(color)
    # Initialize heading
    turtle.left(135)
    # Draw first side
    turtle.down()
    turtle.forward(side)
    # Turn and draw the remaining sides
    for _ in range(2, 9):
        # Turn to second side
        turtle.right(45)
        # Draw second side
        turtle.forward(side)
    # Reset turtle pen
    turtle.fill(False)
    turtle.up()

# 6) Draw a star
def draw_star(side, fill_bool, color):
    '''
    Draws a pentagram star, with the farthest point-to-point distance
    specified with an arg. Starts at bottom-left point, assuming absolute
    starting heading of 90 deg. Can be filled or outlined, with fill bool and
    color passed in as an arg.
    '''
    # Set fill vs. outline and color per args
    turtle.fill(fill_bool)
    turtle.color('white', 'white')
    # Initialize heading
    turtle.left(72)
    # Draws first line
    turtle.down()
    turtle.forward(side)
    # Turns and draws the remaining sides
    for _ in range(2, 6):
        turtle.right(144)
        turtle.forward(side)
    # Reset turtle pen
    turtle.end_fill()
    turtle.up()

# 7) Draw a circle
def draw_circle(radius, extent, steps, fill_bool, color):
    '''
    Draws a circle using the turtle circle() function and passes args on to it.
    Main difference is that this method sets pen down and lifts up at beginning
    and end of drawing, as well as passes a bool for fill / outline and color.
    '''
    # Set fill vs. outline and color per args
    turtle.fill(fill_bool)
    turtle.color(color)
    # Put the pen down
    turtle.down()
    # Draw our circle
    turtle.circle(radius, extent, steps)
    # Reset turtle pen
    turtle.fill(False)
    turtle.up()
