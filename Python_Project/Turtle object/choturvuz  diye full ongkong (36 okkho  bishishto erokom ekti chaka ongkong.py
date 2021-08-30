import turtle
turtle.color("blue")
turtle.speed(7)

counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(120)
        turtle.right(90)
    turtle.right(10)
    counter += 1
turtle.exitonclick()
