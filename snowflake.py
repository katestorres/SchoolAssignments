
import turtle

def thue_morse(n):
    seq = [0]
    while(len(seq)<n):
        temp = seq
        for i in range(len(seq)):
            if(seq[i]==0): temp.append(1)
            else: temp.append(0)
        seq=temp
    return seq[0:(n-1)]

def koch(turt, width, n):
    turt.penup()
    turt.goto(0, 300)
    turt.pendown()
    seq = thue_morse(n)
    for i in seq:
        if(i==0): turt.forward(width)
        else: turt.left(60)

turtle.setup(800, 800)
wn = turtle.Screen()
turt = turtle.Turtle()
turt.speed(0)
koch(turt, 5, 10000)
wn.exitonclick()
