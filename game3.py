#keyboard

import turtle
import keyword
from turtle import *
import math
import random

wn=turtle.Screen()
wn.bgcolor('black')

#border of the game
mypen=turtle.Turtle()
mypen.pensize(5)
mypen.color("white")
mypen.penup()
mypen.setposition(-250,-250)
mypen.pendown()
for x in range(4):
    mypen.forward(500)
    mypen.left(90)
mypen.penup()
mypen.hideturtle()


#hit
c=0
hit=turtle.Turtle()
hit.color('blue')
hit.shape('circle')
hit.penup()
hit.speed(c)
hit.setposition(-50,-100)

tim=turtle.Turtle()
tim.pensize(5)
tim.shape('turtle')
tim.color('red')

speed=1
tim.penup()
def turnleft():
    tim.left(30)
def turnright():
    tim.right(30)
def turnup():
    global speed
    speed+=1

turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(turnup,"Up")

score=0

while(True):
    tim.forward(speed)



    #bounce
    if tim.xcor() > 240 or tim.xcor() < -240:
        tim.right(180)
    if tim.ycor() >240 or tim.ycor() < -240:
        tim.left(180)


    #make hit
    d= math.sqrt(math.pow(tim.xcor()-hit.xcor(),2) + math.pow(tim.ycor()-hit.ycor(),2))

    if d<20:
        hit.setposition(random.randint(-250,250),random.randint(-250,250))
        score=score+1

        sp=score/2
        if sp==0:
            c=c+0.5
            hit.speed(c)

    mypen.undo()
    mypen.penup()
    mypen.hideturtle()
    mypen.setposition(-240,260)
    scoredisp="Score: %s" %score
    mypen.write(scoredisp,False,align="left",font=("Arial",14,"normal"))





    #moving the ball
    hit.forward(1)
    if hit.xcor() > 240 or hit.xcor() < -240:
        hit.right(180)
    if hit.ycor() >240 or hit.ycor() < -240:
        hit.left(180)










