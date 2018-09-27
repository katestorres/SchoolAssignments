import turtle

turtle.setup(800, 800)
wn = turtle.Screen()

ike = turtle.Turtle()

ike.color('green')

ike.penup()

ike.left(270)

ike.forward(300)

ike.right(270)

ike.pendown()

ike.circle(50)

ike.penup()

ike.left(67)

ike.forward(200)

ike.pendown()

ike.color('yellow')

ike.circle(50)

ike.penup()

ike.forward(200)

ike.pendown()

ike.color('red')

ike.circle(50)

wn.exitonclick()
