import turtle
turtle.color("green")
turtle.begin_fill("red")
turtle.speed(7)

counter = 0
while counter < 12:
    for i in range(4):
        turtle.forward(150)
        turtle.right(200)
    turtle.right(70)
    counter += 1
turtle.exitonclick()
