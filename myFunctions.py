def tear(t):
    for times in range(10):
        t.circle(times * 2)
        t.left(10)
        t.forward(10)
        
def L(t,distance,angle):
    t.forward(distance)
    t.left(angle)
    t.forward(distance)
    

def polygon(t, sides, distance):
    angle = 360 / sides
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def cool(t,distance):
    t.color("black")
    polygon(t,4,distance)
    t.color("orange")
    polygon(t,3,distance)

def coolsquared(t):
    for times in range(4):
        cool(t,100)
        t.right(90)

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
                        
def star(t, c):
    t.color(c)
    print(c)
    polygon(t,3,5)
    t.left(200)
