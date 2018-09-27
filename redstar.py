import turtle

turtle.setup(800,800)
wn = turtle.Screen()

nipon = turtle.Turtle()
nipon.color('red')

for i in range(72):
    nipon.forward(200)
    nipon.left(180)
    nipon.forward(200)
    nipon.left(175)

wn.exitonclick()
