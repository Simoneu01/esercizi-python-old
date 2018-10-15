import turtle 
import random

ninja = turtle.Turtle()

ninja.speed(100)
colors=["red","green","blue"]
for i in range(180):
    ninja.color(random.choice(colors))
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()
