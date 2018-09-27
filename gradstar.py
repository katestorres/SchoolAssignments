import turtle

turtle.setup(800,800)
wn = turtle.Screen()

venus = turtle.Turtle()
x=0
venus.color(x,0,1)

for i in range(72):
    venus.forward(200)
    venus.right(180)
    venus.forward(200)
    venus.right(175)
    x=x+.013888
    venus.color(x,0,1)


wn.exitonclick()
