import turtle
turtle.color("green")
turtle.speed(7)

counter = 0
while counter < 12:
    for i in range(4):
        turtle.forward(150)
        turtle.right(120)
    turtle.right(30)
    counter += 1
turtle.exitonclick()
