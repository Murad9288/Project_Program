import turtle
turtle.color("green")
turtle.speed(7)

counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(90)
        turtle.right(120)
    turtle.right(70)
    counter += 1
turtle.exitonclick()
