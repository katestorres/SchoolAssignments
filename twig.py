#"twig" curve
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
    if(ch=="X"):
        newstr = "F+[[X]-X]-F[-FX]+X"
    elif(ch=="F"):
        newstr = "FF"
    else:
        newstr = ch
    return newstr

def twig(berry, width, iter):
    axiom = "X"
    instr = create(axiom, iter)
    saved = []
    for i in instr:
        if(i=='+'):
            berry.right(25)
        elif(i=='-'):
            berry.left(25)
        elif(i=='F'):
            berry.forward(width)
        elif(i=='['):
            saved.append([berry.heading(), berry.xcor(), berry.ycor()])
        elif(i==']'):
            berry.color("light pink")
            berry.forward(width)
            berry.begin_fill()
            berry.circle(width)
            berry.end_fill()
            berry.color("black")
            berry.penup()
            new = saved.pop()
            berry.setheading(new[0])
            berry.setposition(new[1], new[2])
            berry.pendown()

turtle.setup(800, 800)
wn = turtle.Screen()
berry = turtle.Turtle()
berry.speed(0)
berry.penup()
berry.goto(-375,0)
berry.pendown()
twig(berry, 5, 6)
wn.exitonclick()
