import turtle

def unfold_dragon(n):
    seq =[0]
    while(len(seq)<n):
        temp = []
        for i in range(len(seq)):
            temp.append(seq[-(i+1)])
        seq.append(0)
        for i in range(len(temp)):
            if(temp[i]==0):
                temp[i]=1
            else:
                temp[i]=0
        seq=seq+temp
    return seq[0:n]

def dragon(toothless, width, n):
    toothless.pendown()
    seq = unfold_dragon(n)
    for i in seq:
        if(i==0):
            toothless.right(90)
            toothless.forward(width)
        else:
            toothless.left(90)
            toothless.forward(width)

turtle.setup(800, 800)
wn = turtle.Screen()
toothless = turtle.Turtle()
toothless.speed(0)
dragon(toothless, 5, 10000)
wn.exitonclick()
