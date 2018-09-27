import turtle

turtle.setup(800,800)
wn = turtle.Screen()

yeoleturtle = turtle.Turtle()

yeoleturtle.penup()

yeoleturtle.forward(400)

yeoleturtle.left(180)

yeoleturtle.pendown()

for i in range(20):
    yeoleturtle.forward(20)
    yeoleturtle.left(90)
    yeoleturtle.forward(20)
    yeoleturtle.right(90)
    yeoleturtle.forward(20)
    yeoleturtle.right(90)
    yeoleturtle.forward(20)
    yeoleturtle.left(90)

wn.exitonclick()
