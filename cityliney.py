from Towersy import (tower1, tower2, tower3, tower4, tower5)
from Streetsy import (streetPave, street2, moonsy)
import turtle

#adjustments to turtle

turtle.speed(50)
turtle.bgcolor("#1b252d")
turtle.pencolor('')

#These are all my towers;

turtle.penup
turtle.goto(-220, -300)
for i in range(2):
    tower5()
    turtle.fd(400)

turtle.penup
turtle.goto(-380, -300)
for i in range(3):
    tower4()
    turtle.fd(300)

turtle.penup
turtle.goto(-300, -300)
for i in range(2):
    tower1()
    turtle.fd(300)
        
turtle.penup
turtle.goto(-260, -300)
for i in range(2):
    tower3()
    turtle.fd(360)
        
turtle.penup
turtle.goto(-330, -300)
for i in range(3):
    tower2()
    turtle.fd(200)

#These are parts of the street and moon.

turtle.penup
turtle.goto(-360, -290)
for i in range(1):
    streetPave()

turtle.penup
turtle.goto(-360, -300)
street2()

turtle.penup
turtle.goto(270, 260)
turtle.pd
moonsy()

#I use conditions to turn a light on in one of my buildings if the input is "yes"

answer = input("Would you like to stay awake? Yes or No: ")
if answer.lower() == 'yes':
    turtle.fillcolor('#fffedd')
    turtle.penup
    turtle.goto(30, 0)
    turtle.pd
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(20)
        turtle.lt(90)
    turtle.end_fill()
    

elif answer.lower() == 'no':
    print("Ok. Goodnight.")
