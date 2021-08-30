# Turtle diye Sun Art - system=1
'''
import turtle
turtle.color('red','green')
turtle.begin_fill()
turtle.speed(10)
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.position()) < 1:
        break

turtle.end_fill()
turtle.done()
'''
# Turtle diye Sun Art - system=2
'''
from turtle import*
begin_fill()
color('red','yellow')
speed(10)
while True:
    forward(200)
    left(170)
    if abs(position()) < 1:
        break
end_fill()
done()
'''
from turtle import *
begin_fill()
color('red')
speed(10)
circle(200,360)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

end_fill()
done()
