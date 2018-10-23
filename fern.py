
import random, turtle

def barnsley_fern(turt, count):
    x = y = 0
    turt.speed(20)
    turt.color("dark sea green")
    for i in range(count):
        choice = random.randrange(0,100)
        if(choice==0):
            x = 0
            y = stem(turt, y) #full stem portion
        elif(choice >0 and choice<=86):
            x = ltosx(turt, x, y) #find x value
            y = ltosy(turt, x, y) #find y value
            move(turt,x,y) #add dot
        elif (choice >86 and choice<=93):
            x = stolx(turt, x, y) #find x value
            y = stoly(turt, x, y) #find y value
            move(turt, x, y) #add dot
        elif(choice>93):
            x = flipx(turt, x, y) #find y value
            y = flipy(turt, x, y) #find x value
            move(turt, x, y) #add dot


def move(turt,x,y):
    turt.penup()
    turt.goto((x*50), (y*50-300))
    turt.pendown()
    turt.begin_fill()
    turt.circle(1)
    #turt.forward(1)#this looks pretty cool too

def stem(turt, y):
    turt.penup()
    nx = 0
    ny = 0.16*y
    turt.goto(nx, ny)
    turt.pendown()
    turt.begin_fill()
    turt.circle(1)
    #turt.forward(1)
    return ny

def ltosx(turt, x, y):
    return ((0.85*x) + (0.04*y))

def ltosy(turt, x, y):
    return ((-0.04*x) + (0.85*y) + 1.6)

def stolx(turt, x, y):
    return ((0.2*x)-(0.26*y))

def stoly(turt, x, y):
    return ((0.23*x)+(0.24*y)+0.44)

def flipx(turt, x, y):
    return ((-0.15*x)+(0.28*y))

def flipy(turt, x, y):
    return ((0.26*x)+(0.24*y)+0.44)

turtle.setup(800, 800)
wn = turtle.Screen()
turt = turtle.Turtle()
turt.speed(0)
barnsley_fern(turt, 10000)
wn.exitonclick()
