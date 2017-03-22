from myFunctions import *
import turtle

bob = turtle.Turtle()
turtle.colormode(255)
turtle.bgcolor("green")
bob.speed(0)

for times in range(256):
    c = (255-times,255-times,255-times)
    star(bob,c)
    bob.forward(times)

jump(bob,200,200)
for times in range(256):
    c = (255-times,255-times,0)
    star(bob,c)
    bob.forward(times)
    
jump(bob,200,-200)
for times in range(256):
    c = (255-times,0,0)
    star(bob,c)
    bob.forward(times)

jump(bob,-200,-200)
for times in range(256):
    c = (255-times,0,255-times)
    star(bob,c)
    bob.forward(times)

jump(bob,-200,200)
for times in range(256):
    c = (0,255-times,255-times)
    star(bob,c)
    bob.forward(times)

