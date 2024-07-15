from turtle import Turtle, Screen
import random


# def draw_shape(sides):
#     angle = 360 / sides
#     t.color(random.random(), random.random(), random.random())
#
#     for _ in range(sides):
#         t.forward(100)
#         t.right(angle)


t = Turtle()
t.speed('fastest')
num_circles = 60

for _ in range(num_circles):
    t.color(random.random(), random.random(), random.random())
    t.circle(100)
    t.left(360 / num_circles)

screen = Screen()
screen.colormode(255)
screen.exitonclick()
