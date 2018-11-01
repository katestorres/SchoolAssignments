#"herb" curve
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
    if(ch=="H"):
        newstr = "HFX[+H][-H]"
    elif(ch=="X"):
        newstr = "X[-FFF][+FFF]FX"
    else:
        newstr = ch
    return newstr

def herb(thyme, width, iter):
    axiom = "H"
    instr = create(axiom, iter)
    saved = []
    for i in instr:
        if(i=='+'):
            thyme.right(25.7)
        elif(i=='-'):
            thyme.left(25.7)
        elif(i=='F'):
            thyme.forward(width)
        elif(i=='['):
            saved.append([thyme.heading(), thyme.xcor(), thyme.ycor()])
        elif(i==']'):
            thyme.penup()
            new = saved.pop()
            thyme.setheading(new[0])
            thyme.setposition(new[1], new[2])
            thyme.pendown()

turtle.setup(800, 800)
wn = turtle.Screen()
thyme = turtle.Turtle()
thyme.speed(0)
thyme.penup()
thyme.goto(-375,0)
thyme.pendown()
herb(thyme, 5, 8)
wn.exitonclick()
