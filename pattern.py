#This is supposed to look like
#4 rows of 8-pointed stars
import turtle

turtle.setup(800,800)
wn = turtle.Screen()

dizzy = turtle.Turtle()
brizzy = turtle.Turtle()
dizzy.penup()
brizzy.penup()
dizzy.left(180)
brizzy.left(180)
dizzy.forward(400)
brizzy.forward(400)
brizzy.left(90)
dizzy.right(90)
dizzy.forward(250)
brizzy.forward(150)
brizzy.left(90)
dizzy.right(90)
dizzy.pendown()
brizzy.pendown()
brizzy.color('IndianRed')
dizzy.color('wheat')
for i in range(2):
    for i in range(5):
        for i in range(8):
            dizzy.forward(60)
            brizzy.forward(60)
            dizzy.left(45)
            brizzy.left(45)
            dizzy.forward(60)
            brizzy.forward(60)
            dizzy.left(135)
            brizzy.left(135)
            dizzy.forward(60)
            brizzy.forward(60)
            dizzy.left(45)
            brizzy.left(45)
            dizzy.forward(60)
            brizzy.forward(60)
            dizzy.left(180)
            brizzy.left(180)
        dizzy.penup()
        brizzy.penup()
        dizzy.forward(200)
        brizzy.forward(200)
        dizzy.pendown()
        brizzy.pendown()
    dizzy.penup()
    brizzy.penup()
    dizzy.left(180)
    brizzy.left(180)
    dizzy.forward(200)
    brizzy.forward(200)
    dizzy.left(90)
    brizzy.left(90)
    dizzy.forward(200)
    brizzy.forward(200)
    dizzy.right(90)
    brizzy.right(90)
    dizzy.pendown()
    brizzy.pendown()

wn.exitonclick()
