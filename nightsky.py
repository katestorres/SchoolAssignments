
import random
import turtle

# This function draws the entire night sky using turtle turt.
def draw_sky(turt):
    turt.speed(20)
    # draw 200 random stars, one by one
    for speck in range(200):
        turt.penup()
        # choose random x and y coordinates
        # TODO: you need to rewrite these statements to generate coordinates
        # over the entire window, not just near the origin
        x = random.randrange(-400, 400)
        y = random.randrange(-400, 400)

        # choose random star type; first generate an integer between
        # 0 and 99 inclusive
        percent = random.randrange(0, 100)
        if percent >= 0 and percent <= 60:
            blue_star(turt, x, y)
        elif percent > 60 and percent <=93:
            red_star(turt, x,y)
        else:
            big_star(turt,x,y)
        # TODO: now use if statement(s) on percent, to decide whether to
        # call blue_star, white_star, or big_star
    x = random.randrange(-400, 400)
    y = random.randrange(-400, 400)
    rocket(turt, x, y)
    turt.penup()
    turt.color(0,0, .1)
    turt.forward(20)    

# Draw a small blue star at x, y, using turt.
def blue_star(turt, x, y):
    turt.goto(x, y)
    # TODO: add statements to pick a random blue-white color, and random
    # radius, and then draw a dot using that color and radius
    colors = ["white smoke", "gainsboro", "alice blue", "azure",
            "honeydew", "ghost white"]
    color = random.choice(colors)
    turt.color(color)
    radius = random.randrange(1, 3)
    turt.pendown()
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()

# Draw a medium-sized red star at x, y using turt.
def red_star(turt, x, y):
    turt.goto(x, y)
    # TODO: add statements to pick a random red-white color, and random
    # radius, and then draw a dot using that color and radius
    colors = ["linen", "seashell", "misty rose", "bisque",
            "light salmon", "peach puff", "light pink"]
    color = random.choice(colors)
    turt.color(color )
    radius = random.randrange(4, 6)
    turt.pendown()
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()

# Draw a large four-pointed star at x, y using turt.
def big_star(turt, x, y):
    turt.goto(x, y)

    # TODO: add statements to draw a four-pointed white star
    turt.color("white")
    length = random.randrange(6, 10)
    turt.pendown()
    turt.begin_fill()
    turt.circle(length, 90)
    turt.left(180)
    turt.circle(length, 90)
    turt.right(180)
    turt.circle(length, 90)
    turt.left(180)
    turt.circle(length, 90)
    turt.right(180)
    turt.end_fill()

def rocket(turt, x, y):
    turt.penup()
    turt.goto(x, y)
    turt.color("Indian Red")
    #cone
    turt.begin_fill()
    turt.forward(10)
    turt.left(120)
    turt.forward(10)
    turt.left(120)
    turt.forward(10)
    turt.end_fill()
    #body
    turt.color("light steel blue")
    turt.penup()
    turt.left(180)
    turt.forward(2)
    turt.left(90)
    turt.pendown()
    turt.begin_fill()
    turt.forward(10)
    turt.right(90)
    turt.forward(6)
    turt.right(90)
    turt.forward(10)
    turt.right(90)
    turt.forward(6)
    turt.end_fill()
    turt.penup()
    #window
    turt.left(180)
    turt.forward(4)
    turt.left(90)
    turt.forward(2)
    turt.color("lemon chiffon")
    turt.begin_fill()
    turt.circle(1)
    turt.end_fill()
    turt.penup()
    #end thing
    turt.right(90)
    turt.forward(2)
    turt.left(90)
    turt.forward(8)
    turt.color("medium aquamarine")
    turt.pendown()
    turt.begin_fill()
    turt.right(45)
    turt.forward(4)
    turt.left(135)
    turt.forward(11)
    turt.left(135)
    turt.forward(4)
    turt.left(45)
    turt.forward(7)
    turt.end_fill()


turtle.setup(800, 800)

# dark navy blue background
turtle.bgcolor((0, 0, .1))

wn = turtle.Screen()
turt = turtle.Turtle()
draw_sky(turt)
wn.exitonclick()
