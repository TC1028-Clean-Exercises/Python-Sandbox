"""
Draw squares of different colors in a gradient pattern

Gilberto Echeverria
2021-09-03
"""


import sys
import turtle


def draw_rectangle(width, height, color):
    """ A colored rectangle """
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def set_position(x, y):
    """ Move to a different position """
    turtle.speed(0)
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()


def draw_gradient(steps, y, height, color_index):
    """ Draw rectangles while changing colors """
    step_width = turtle.window_width() // steps
    half_width = turtle.window_width() / 2
    color_step = 1 / steps
    for step in range(steps):
        x = -half_width + step_width * step
        #print(f"Position: {x}, {y}")
        set_position(x, y)
        # Compute the color for the channel indicated as color_index
        color = tuple((1 if i == color_index
                       else 1 - color_step * step for i in range(3)))
        #print(f"Color: {color}")
        draw_rectangle(step_width, height, color)


def draw_rows(steps):
    """ Show multiple rows, with a different color each """
    num_rows = 4
    step_height = turtle.window_height() // num_rows
    half_height = turtle.window_height() / 2
    # Loop over the 3 primary colors (red, green, blue)
    for row in range(num_rows):
        y = -half_height + step_height * row
        draw_gradient(steps, y, step_height, row)


def get_inputs():
    """ Get the number of steps from the command line """
    if len(sys.argv) == 2:
        steps = int(sys.argv[1])
    else:
        steps = 10
    return steps


def main():
    """ Program start """
    steps = get_inputs()
    draw_rows(steps)
    turtle.done()


main()
