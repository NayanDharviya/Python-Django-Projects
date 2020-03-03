import turtle 
import time
import random
from tkinter import messagebox
delay=0.1

#score
score=0
highscore=0


#set up the screen
tt=turtle.Screen()
tt.setup(width=450,height=400)
tt.bgcolor('red')
tt.tracer(0)  #THIS IS USED FOR SHOWING STARTING POINT .... HOW SCREEN IS DRAW AND BACKGROUND COLOR AND ALL DEFAULT


#create boundry so that user know
left=turtle.Turtle()
left.speed(0)
left.color('white')
left.penup()
left.goto(-235,-210)
left.hideturtle()
left.pendown()
left.goto(235,-210)
left.goto(235,210)
left.goto(-235,210)
left.goto(-235,-210)


#show score on screen
p=turtle.Turtle()
p.speed(0)
p.shape('square')
p.color('white')
p.penup()
p.hideturtle()
p.goto(0,160)
p.write('Score:0  High Score:0',align="center",font=("Times New Roman",24,"normal"))

#snake head
head=turtle.Turtle()
head.direction='stop'
head.color('blue')
head.shape('square')
head.penup()
head.goto(0,20)
head.direction='stop'

#head.speed(0)
#move snake

#snake food
food=turtle.Turtle()
food.shape('circle')
food.color('yellow')
food.penup()
food.goto(0,100)
food.speed(0)

segments=[]


#functions

def go_up():
    if head.direction!='down':
        head.direction='up'

def go_down():
    if head.direction!='up':
        head.direction='down'

def go_left():
    if head.direction!='right':
        head.direction='left'

def go_right():
    if head.direction!='left':
        head.direction='right'





#on movements turtle should move how much steps and in which direction
def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)

    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)

    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)

    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)

#keyboard connection
tt.listen()
tt.onkeypress(go_up,'Up')   #for up arrow
tt.onkeypress(go_down,'Down') #for down arrow
tt.onkeypress(go_left,'Left') #for left arrow
tt.onkeypress(go_right,'Right') #for right arrow


while True:
    
    
    tt.update()

        

    
    #set end border of the screen
    if head.xcor()>225 or head.xcor()<-225 or head.ycor()>200 or head.ycor()<-200:
        messagebox.showinfo('Over','Game Over!!')
        time.sleep(0)
        head.direction ='stop'
        head.goto(0,0)
        #hide the segment
        for n in segments:
            n.goto(1000,1000)
        #clear the segment list
        segments.clear()

        #reset the code
        score=0

        #reset the delay
        delay=0.1
        p.clear()  
        p.write('Score:{}  High Score:{}'.format(score,highscore),align="center",font=("Times New Roman",24,"normal"))  
        

    #check head collision with segment
    for n in segments:
        if n.distance(head)<20:
            messagebox.showinfo('Over','Game Over!!')
            time.sleep(0)
            head.direction='stop'
            head.goto(0,0)
            
            #hide the segment
            for n in segments:
                n.goto(1000,1000)

            #clear the segment list
            segments.clear()

             #reset the code
            score=0

            #reset the delay
            delay=0.1

            #update the score
            p.clear()
            p.write('Score:{}  High Score:{}'.format(score,highscore),align="center",font=("Times New Roman",24,"normal"))  
            #score+=10

            

    
    
    #check for collision with the food
    if head.distance(food)<20:
        #tranfer the foor to random position
        x=random.randint(-225,225)
        y=random.randint(-200,200)
        food.goto(x,y)

        #add new segment which add after snake eat food
        c=['blue','pink','yellow','grey','green','violet','white']
       
        new_seg=turtle.Turtle()
        co=random.choice(c)
       
        new_seg.speed(0)
        new_seg.color(co)
        new_seg.shape('square')
        new_seg.penup()

        segments.append(new_seg)
        print(len(segments))
        delay-=0.001

        #increase the score
        score+=10
        if score>highscore:
            highscore=score
        p.clear()
        p.write('Score:{}  High Score:{}'.format(score,highscore),align="center",font=("Times New Roman",24,"normal"))  
        #move last segment to first

    for index in range(len(segments)-1,0,-1):
        #means it will execute untill first segment of snake is move
        #it is like practically move last segment of snake but using this loop we move all the previous segments of snake
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

        #move segment at where head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
            
    move()
    time.sleep(delay)
tt.mainloop()
