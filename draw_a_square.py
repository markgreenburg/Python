from turtle import *
print __name__

def draw_a_square(length):
    '''draw a square of defined length.'''
    for i in range(4):
        forward(length)
        left(90)
        
if __name__=="__main__":
    draw_a_square(100)



    draw_a_square(100)
