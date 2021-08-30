import turtle

class AjobTurtle(turtle.Turtle):
    """AjobTurtle is a class for new type of turtle"""
    def forward(self, pixel):
        super().backward(pixel)

    def backward(self, pixel):
        super().forward(pixel)

    def left(self, angle):
        super().right(angle)


    def right(self, angle):
        print("I won't turn right, because I an ajob!")


if __name__ == "__main__":
    montu = AjobTurtle()
    montu.left(90)
    montu.forward(200)
    montu.left(90)
    montu.backward(200)
    montu.right(90)
    montu.forward(10)

    jhontu = turtle.Turtle()
    jhontu.shape("turtle")
    jhontu.left(90)
    jhontu.forward(200)
    jhontu.left(90)
    jhontu.backward(200)
    jhontu.right(90)
    jhontu.forward(10)

    turtle.done()
