'''
This script tests all of the methods in the turtle_graphics module in sequence
'''
import turtle as turtle
import turtle_graphics as turtle_shapes

# pylint: disable=no-member
# ^ disable errors for turtle not having the below methods, as they're
#   created dynamically


def draw_shapes_test(side_length, fill_bool, color):
    '''
    Tests methods from turtle_graphics module in sequence with side length
    passed in as arg. Output should be a series of drawings, each
    originating and ending at the same point.
    '''
    # Test equilateral triangle drawing
    turtle_shapes.draw_equilateral(side_length, fill_bool, color)

    # Reset to default heading
    turtle.seth(0)

    # Test square drawing
    turtle_shapes.draw_square(side_length, fill_bool, color)

    # Reset to default heading
    turtle.seth(0)

    # Test pentagon drawing
    turtle_shapes.draw_pentagon(side_length, fill_bool, color)

    # Reset to default heading
    turtle.seth(0)

    # Test hexagon drawing
    turtle_shapes.draw_hexagon(side_length, fill_bool, color)

    # Reset to default heading
    turtle.seth(0)

    # Test octagon drawing
    turtle_shapes.draw_octagon(side_length, fill_bool, color)

    # Reset to default heading
    turtle.seth(0)

    # Test star drawing
    turtle_shapes.draw_star(side_length, fill_bool, color)

# Call the test function
draw_shapes_test(150, True, "Green")
