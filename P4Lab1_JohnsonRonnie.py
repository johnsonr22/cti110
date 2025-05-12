#Ronnie Johnson
#3/19/2025
#P4LAB1
#Turtle graphics program to draw triangle and square

import turtle
win = turtle.Screen()
win.bgcolor('black')
t = turtle.Turtle()

#Set the way timmy looks
t.pensize(6)
t.pencolor('red')
t.shape('circle')


#Test
#t.forward(100)

#for loop that runs 4 times
for i in range(4):
    print(i)
    t.forward(100)
    t.right(90)


#while loop that runs 3 times
this_run=0
while this_run<3:
    t.forward(100)
    t.left(120)
    this_run+=1
#while this_run <3:


#Keeps the window open after shape is drawn
win.mainloop()