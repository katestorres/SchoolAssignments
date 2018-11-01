#hilbert curve
import turtle

def create(axiom, iter):
    startString = axiom
    endString = ""
    for i in range(iter):
        endString = process(startString)
        startString = endString
    return endString

def process(oldStr):
    newstr = ""
    for i in oldStr:
        newstr = newstr + apply(i)
    return newstr

def apply(ch):
    newstr = ""
    if(ch=="L"):
        newstr = "+RF-LFL-FR+"
    elif(ch=="R"):
        newstr = "-LF+RFR+FL-"
    else:
        newstr = ch
    return newstr

def hilbert(david, width, iter):
    axiom = "L"
    instr = create(axiom, iter)
    for i in instr:
        if(i=='+'):
            david.right(90)
        elif(i=='-'):
            david.left(90)
        elif(i=='F'):
            david.forward(width)


turtle.setup(800, 800)
wn = turtle.Screen()
david = turtle.Turtle()
david.speed(0)
david.penup()
david.goto(-375,300)
david.pendown()
hilbert(david, 5, 8)
wn.exitonclick()
