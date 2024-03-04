# import colorgram
#
# extracted_colors = colorgram.extract('hirst_spot_painting.jpg', 100)
# extracted_colors.pop(0)
#
# extracted_rgb = []
# for n in extracted_colors:
#     r = n.rgb.r
#     g = n.rgb.g
#     b = n.rgb.b
#     extracted_rgb.append((r, g, b))
# print(extracted_rgb)

# Import packages
import turtle as t
import random

# Initialize the turtle, distance globals
tim = t.Turtle()
t.colormode(255)
RADIUS = 10
HORIZ_SPACE = 50
CANVAS_SIDE = RADIUS * 2 * 10 + HORIZ_SPACE * 9
HORIZ_MOVE = 50 + RADIUS * 2

# Set the list of colors to be used for dots, extracted using colorgram
color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71),
              (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229),
              (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9),
              (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155), (238, 157, 212),
              (86, 77, 208), (86, 225, 235), (250, 8, 14), (242, 166, 157), (177, 180, 224), (36, 243, 159),
              (6, 81, 115), (11, 55, 248)]


# Set turtle attributes
def set_turtle_attributes():
    tim.speed("fastest")
    tim.pensize(1)
    tim.up()
    tim.hideturtle()


# Set color
def choose_color():
    return random.choice(color_list)


# Move to starting position
def move_to_start():
    tim.right(180)
    tim.forward(CANVAS_SIDE / 2)
    tim.left(90)
    tim.forward(CANVAS_SIDE / 2)


# Move to next horizontal space
def move_horizontal():
    tim.left(90)
    tim.forward(HORIZ_MOVE)
    tim.right(90)


# Move to next vertical line
def move_vertical():
    tim.right(90)
    tim.forward(CANVAS_SIDE + HORIZ_MOVE - RADIUS * 2)
    tim.right(90)
    tim.forward(HORIZ_MOVE)
    tim.right(180)


# Main program loop
set_turtle_attributes()
move_to_start()
for _ in range(10):
    for _ in range(10):
        current_color = choose_color()
        tim.pencolor(current_color)
        tim.dot(RADIUS * 2, current_color)
        move_horizontal()
    move_vertical()

# Build screen, set attributes
screen = t.Screen()
screen.exitonclick()
