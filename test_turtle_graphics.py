'''
This script tests all of the methods in the turtle_graphics module in sequence
'''
import turtle_graphics as turtle_shapes
import turtle as turtle

# pylint: disable=no-member
# ^ disable errors for turtle not having the below methods, as they're
#   created dynamically


def draw_shapes_test(side_length):
    '''
    Tests methods from turtle_graphics module in sequence with side length
    passed in as arg. Output should be a series of drawings, each
    originating and ending at the same point.
    '''
    # Test equilateral triangle drawing
    turtle_shapes.draw_equilateral(side_length)

    # Reset to default heading
    turtle.seth(0)

    # Test square drawing
    turtle_shapes.draw_square(side_length)

    # Reset to default heading
    turtle.seth(0)

    # Test pentagon drawing
    turtle_shapes.draw_pentagon(side_length)

    # Reset to default heading
    turtle.seth(0)

    # Test hexagon drawing
    turtle_shapes.draw_hexagon(side_length)

    # Reset to default heading
    turtle.seth(0)

    # Test octagon drawing
    turtle_shapes.draw_octagon(side_length)

    # Reset to default heading
    turtle.seth(0)

    # Test star drawing
    turtle_shapes.draw_star(side_length)

# Call the test function
draw_shapes_test(150)
