import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(132, 167, 207), (209, 132, 143),
              (135, 183, 156), (209, 83, 100), (32, 36, 54), (157, 16, 32), (217, 159, 113), (53, 111, 160),
              (171, 186, 218), (137, 68, 81), (31, 61, 55), (103, 119, 175), (50, 42, 46), (43, 109, 87),
              (219, 217, 99), (150, 58, 50), (24, 61, 117), (238, 176, 151), (56, 55, 50), (220, 100, 49),
              (16, 102, 62), (228, 170, 177), (166, 202, 213), (42, 148, 203), (175, 201, 185), (109, 138, 123)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1 , number_of_dots + 1):
    tim.dot(20 , random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)











screen = turtle_module.Screen()
screen.exitonclick()