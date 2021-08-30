import turtle
from random import randint
 
window = turtle.Screen()
turtle.bgcolor("black")
turtle.color("yellow")
turtle.speed(0)
 
def draw_star():
    turns = 6
    turtle.begin_fill()
    while turns>0:
        turtle.forward(25)
        turtle.left(145)
        turns = turns-1
    turtle.end_fill()
 
nums_stars = 0
while nums_stars <50:
    x=randint(-300,300)
    y=randint(-300,300)
    draw_star()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    nums_stars = nums_stars + 1
 
window.exitonclick()
