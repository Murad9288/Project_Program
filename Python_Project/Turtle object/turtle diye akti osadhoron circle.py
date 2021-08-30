import turtle
turtle.color("blue")
turtle.speed(5)
counter = 0
while counter < 2:
    for i in range(2):
        turtle.forward(60)
        turtle.right(45)
        turtle.right(25)
        turtle.forward(35)
    turtle.right(5)
turtle.exitonclick()
