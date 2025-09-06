# Making the Hirst painting

'''
import colorgram 

rgb_colors = []
colors = colorgram.extract('./Day18/image.jpg', 30)

def remove_whites(colors: list, threshold=220):
    return [color for color in colors if not all(c >= threshold for c in color)]

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_colors.append(rgb)

rgb_colors = remove_whites(rgb_colors)
'''
# used the above code to obtain the colors_to_use
import turtle
import random

turtle.colormode()

t = turtle.Turtle()
t.shape("classic")


colors_to_use = [(215, 166, 17), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56)]

def rgb_to_hex(rgb):
    """
    Converts an (R, G, B) tuple to a hex color string.
    Example: (94, 183, 167) → '#5EB7A7'
    """
    return '#{:02X}{:02X}{:02X}'.format(*rgb)

converted_to_hex = [rgb_to_hex(rgb) for rgb in colors_to_use]

t.teleport(-150, -80) # starting position

def draw_pattern():
    for i in range(10):
        t.dot(10, random.choice(converted_to_hex))
        t.penup()
        t.forward(30)
        t.pendown()

y_increment = 30
for i in range(10):
    draw_pattern()
    t.teleport(-150, y_increment - 80)
    y_increment += 30

screen = turtle.Screen()
screen.exitonclick()