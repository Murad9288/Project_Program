from turtle import *
import turtle

height = 1000
width = 720
screen = Screen()
screen.screensize(width, height)

# Moon 
moon = turtle.Turtle()
eid = turtle.Turtle()
eid.reset()
moon.reset()
eid.pensize(10)
#moon.speed(100)

def eid_moon():    
    moon.up()
    moon.goto(-450,80)
    moon.color('black')
    moon.begin_fill()
    moon.circle(200)
    moon.end_fill()
    
    moon.up()
    moon.goto(-420,110)
    moon.color('white')
    moon.begin_fill()
    moon.circle(200)
    moon.end_fill()

eid_moon()


# Border
star_bor = turtle.Turtle()

star_bor.reset()
star_bor.speed(50000)
star_bor.penup()
star_bor.goto(850,0)
star_bor.left(90)
star_bor.pendown()
def starr(size):
    for i in range(5):
        star_bor.forward(size/7)
#       star(turtle, size/3)
        star_bor.left(216)
for i in range(100):
        starr(200)
        star_bor.forward(450/100)
        
star_bor.left(90)
for i in range(400):
        starr(200)
        star_bor.forward(1700/400)

star_bor.left(90)
for i in range(200):
        starr(200)
        star_bor.forward(900/200)

star_bor.left(90)

for i in range(400):
        starr(200)
        star_bor.forward(1700/400)

star_bor.left(90)
for i in range(100):
        starr(200)
        star_bor.forward(450/100)


# Star
sta = turtle.Turtle()

sta.reset()
sta.speed(100)
sta.pensize(2)

# multiple star
sta.penup()
sta.goto(-600,400)
sta.right(90)
sta.forward(500)
sta.pendown()

def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
        
star(sta, 200)


staa = turtle.Turtle()
staa.reset()
staa.speed(5)
staa.pensize(4)
# star
staa.penup()
staa.goto(-150,400)
staa.right(90)
staa.pendown()

def starrr(size):
    for i in range(5):
        staa.forward(size/7)
#       star(turtle, size/3)
        staa.left(216)
    

staa.penup()
staa.forward(400)
staa.pendown()
starrr(800)


staa.left(90)
staa.penup()
staa.forward(700)
staa.pendown()
starrr(1200)

staa.left(155)
staa.penup()
staa.forward(900)
staa.pendown()
starrr(400)

staa.right(180)
staa.penup()
staa.forward(450)
staa.pendown()
starrr(1000)

staa.right(155)
staa.penup()
staa.forward(900)
staa.pendown()
starrr(400)

staa.left(180)
staa.penup()
staa.forward(350)
staa.left(90)
staa.forward(100)
staa.pendown()
starrr(400)

staa.right(95)
staa.penup()
staa.forward(350)
staa.left(90)
staa.forward(50)
staa.pendown()
starrr(800)

staa.right(180)
staa.penup()
staa.forward(100)
staa.right(90)
staa.forward(50)
staa.pendown()
starrr(600)




# Eid mubarak
def latter_e(height):
#    eid.color('red')
#    eid.begin_fill()
    
    eid.forward(100) #1
    e_endPos = eid.position()
    
    eid.left(90)
    eid.forward(30) #2
    
    eid.left(90)
    eid.forward(70) #3 
    
    eid.right(90) #4
    eid.forward(30)
    
    eid.right(90) #5
    eid.forward(65)
    
    eid.left(90) #6
    eid.forward(30)
    
    eid.left(90) #7
    eid.forward(65)
    
    eid.right(90) #8
    eid.forward(30)
    
    eid.right(90) #9
    eid.forward(70)
    
    eid.left(90) #10
    eid.forward(30)
    
    eid.left(90) #11
    eid.forward(100)
    
    eid.left(90) #12
    eid.forward(150)
#    eid.end_fill()
    eid.setpos(e_endPos)
    eid.left(90)
    
    

   
eid.penup()
eid.goto(-190+200,-100-50)
eid.pendown()
latter_e(150)

def gap_for_eid_mubarak(val):
    eid.penup()
    eid.forward(val)
    eid.pendown()

gap_for_eid_mubarak(30)
# I


def latter_i(height):
#    eid.begin_fill()
    eid.forward(100) #1
    i_endPos = eid.position()
    
    eid.left(90)
    eid.forward(30) #2
    
    eid.left(90)
    eid.forward(35) #3 
    
    eid.right(90)
    eid.forward(90) #4 
    
    eid.right(90)
    eid.forward(35) #5 
    
    eid.left(90)
    eid.forward(30) #6
    
    eid.left(90)
    eid.forward(100) #7
    
    eid.left(90)
    eid.forward(30) #8
    
    eid.left(90)
    eid.forward(35) #9
    
    eid.right(90)
    eid.forward(90) #10
    
    eid.right(90)
    eid.forward(35) #12
    
    eid.left(90)
    eid.forward(30) #13
#    eid.end_fill()
    eid.setpos(i_endPos)
    eid.left(90)
   
latter_i(150)
gap_for_eid_mubarak(30)

# D
def latter_d(height):
    eid.color('black')
#    eid.begin_fill()
    
    eid.left(90)
    eid.forward(height)
    eid.right(90)
    
    eid.forward(20)
    
    eid.circle(-height / 2, 180, 30)
    eid.forward(20)
#    eid.end_fill()
    
    
    eid.penup()
    eid.backward(30)
    eid.right(90)
    eid.forward((height - 70) / 2)
    eid.pendown()
    

#    eid.begin_fill()
#    eid.color('white')
    eid.forward(70)
    eid.right(90)
    eid.circle(-70 / 2, 180, 30)
#    eid.end_fill()
    
latter_d(150)

# M
eid.penup()
eid.color('black')
eid.goto(-470+200,-330-50)
eid.left(180)
eid.pendown()

def latter_m(height): 
#    eid.color('red')
#    eid.begin_fill()
    eid.left(90)
    eid.forward(height) #1
    
    eid.right(90)
    eid.forward(20) #2
    
    eid.right(45)
    eid.forward(70) #3
    
    eid.left(90)
    eid.forward(70) #4
    
    eid.right(45)
    eid.forward(20) #5
    
    eid.right(90)
    eid.forward(height) #6
    m_endPos = eid.position()
    
    eid.right(90)
    eid.forward(40) #7
    
    eid.right(90)
    eid.forward(85) #8
    
    eid.left(135)
    eid.forward(40) #9
    
    eid.right(90)
    eid.forward(40) #10
    
    eid.left(135)
    eid.forward(85) #11
    
    eid.right(90)
    eid.forward(45) #7
    
    eid.penup()
    eid.setpos(m_endPos)
    eid.left(180)
    eid.pendown()
    
#    eid.end_fill()
    
latter_m(150)

gap_for_eid_mubarak(15+5)



# U
def latter_u(height,width):
#    eid.color('red')
#    eid.begin_fill()
    
    eid.left(90)
    eid.forward(height) #1
    
    eid.right(90)
    eid.forward(width/3) #2

    eid.right(90)
    eid.forward(height - height/4) #3

    eid.left(90)
    eid.forward(width/3) #4

    eid.left(90)
    eid.forward(height - height/4) #5  
    
    eid.right(90)
    eid.forward(width/3) #6   
    
    eid.right(90)
    eid.forward(height) #7  
    u_endPos = eid.position()
    
    
    eid.right(90)
    eid.forward(width) #1 
#    eid.end_fill()
    
    eid.setpos(u_endPos)
    eid.left(180)
    

latter_u(150,140)

gap_for_eid_mubarak(15+5)

# B
def latter_b(height,width):
#    eid.color('red')
#    eid.begin_fill()
    
    b_sPos = eid.position()
    
    eid.left(90)
    eid.forward(height) #1
    
    eid.right(90)
    eid.forward(width/3) #2
    
    eid.circle(-height / 4, 180, 30) #3
    
    eid.right(180)
    eid.circle(-height / 4, 180, 30) #4
    
    eid.forward(width/3) #5
#    eid.end_fill()
    
    eid.penup()
    eid.backward(width/4)
    eid.right(90)
    eid.forward(height/8)
    eid.pendown()
    
#    eid.color('red','white')
#    eid.begin_fill()
    eid.forward((height/8)*2)
    eid.right(90)
    eid.circle((-(height/8)*2) / 2, 180, 30)
#    eid.end_fill()
    
    eid.right(90)
    eid.penup()
    eid.forward((height/8)*4)
    eid.pendown()
    
#    eid.color('red','white')
#    eid.begin_fill()
    eid.forward((height/8)*2)
    eid.right(90)
    eid.circle((-(height/8)*2) / 2, 180, 30)
#    eid.end_fill()
    
    eid.penup()
    eid.setpos(b_sPos)
    eid.left(180)
    
    
latter_b(150,140)

# A
eid.forward(70)
eid.pendown()
gap_for_eid_mubarak(20+5)


def latter_a(height,width):
#    eid.color('red')
#    eid.begin_fill()
    
    eid.left(75)
    eid.forward(height) #1
    
    eid.right(75)
    eid.forward(width/2) #2
    
    eid.right(75)
    eid.forward(height) #3
    a_endPos = eid.position()
    
    
    eid.right(105)
    eid.forward(width/3) #4
    
    eid.right(75)
    eid.forward(height/4) #5
    
    eid.left(75)
    eid.forward(width/4) #6
    
    eid.left(75)
    eid.forward(height/4) #7
    
    eid.right(75)
    eid.forward(width/3) #8
#    eid.end_fill()
    
    eid.penup()
    eid.backward(width/2)
    eid.right(90)
    eid.forward((height/3)*2.2)
    eid.pendown()
    
#    eid.color('red','white')
#    eid.begin_fill()
    eid.right(90)
    for _ in range(3):
        eid.right(60)
        eid.forward(height/3.5)
        eid.right(60)
#    eid.end_fill()
    
    eid.penup()
    eid.setpos(a_endPos)
    
    
latter_a(150,125)

gap_for_eid_mubarak(8+5)
# R
def latter_r(height,width):
    r_endPos = eid.position()
#    eid.color('red')
#    eid.begin_fill()
    
    eid.left(90)
    eid.forward(height) #1
    
    eid.right(90)
    eid.forward(width/2) #2
    
    eid.circle(-height / 4, 180, 30) #3
    
    eid.left(135)
    eid.forward(height/1.4) #4
    
    eid.right(135)
    eid.forward(width/2.5) #5
    
    eid.right(45)
    eid.forward(height/3) #6
    
    eid.left(135)
    eid.forward(height/4.3) #7
    
    eid.right(90)
    eid.forward(width/2.5) #8
#    eid.end_fill()
    
    
    eid.penup()
    eid.backward(width/4)
    eid.right(90)
    eid.forward((height/4)*2.5)
    eid.pendown()
    
#    eid.color('red','white')
#    eid.begin_fill()
    eid.forward((height/8)*2)
    eid.right(90)
    eid.forward(width/6)
    eid.circle((-(height/8)*2) / 2, 180, 30)
    eid.forward(width/6)
#    eid.end_fill()
    
    eid.penup()
    eid.setpos(r_endPos)
    eid.left(180)
    
latter_r(150,140)

eid.forward(115)
eid.pendown()
gap_for_eid_mubarak(35+5)

# A A
latter_a(150,125)

gap_for_eid_mubarak(16)

## k
def latter_k(height,width):
#    eid.color('red')
#    eid.begin_fill()
    
    eid.left(90)
    eid.forward(height) #1
    
    eid.right(90)
    eid.forward(width/4) #2
    
    eid.right(90)
    eid.forward((height / 7)*3) #3
    
    eid.left(135)
    eid.forward((width/4)*2) #4
    
    eid.right(135)
    eid.forward(width / 4) #5
    
    eid.right(45)
    eid.forward((width / 4)* 1.5) #6
    
    eid.left(90)
    eid.forward((width / 4)*2.5) #7
    
 
    
    eid.right(135)
    eid.forward(width / 4)  #8
    
    eid.right(45)
    eid.forward((width / 4)*1.5) #9
    
    eid.left(135)
    eid.forward(width/4) #10
    
    eid.right(90)
    eid.forward(width/4) #11
#    eid.end_fill()
    
latter_k(150,140)



mess = turtle.Turtle()
mess_b = turtle.Turtle()
mess_bb = turtle.Turtle()


#mess.up()
def mess_b1():
        mess_b.reset()
        mess_b.pensize(5)
        mess_b.speed(5)
        mess_b.penup()
        mess_b.goto(480,370)
        mess_b.pendown()
        
        mess_b.forward(190)

        mess_b.right(90)
        mess_b.forward(140)
        
        mess_b.right(90)
        mess_b.forward(190)
        
        mess_b.right(90)
        mess_b.forward(140)
        mess_b.right(90)

 
def mess_b2():
        mess_bb.reset()
        mess_bb.pensize(5)
        mess_bb.speed(5)
        mess_bb.penup()
        mess_bb.goto(470,380)
        mess_bb.pendown()
        mess_bb.forward(210)
        
        mess_bb.right(90)
        mess_bb.forward(160)
        
        mess_bb.right(90)
        mess_bb.forward(210)
        
        mess_bb.right(90)
        mess_bb.forward(160)
        mess_bb.right(90)


#mess.down()

def mess_logo():
    mess.reset()
    mess.up()
    mess.goto(500,350)
    mess.right(90)
    mess.down()
    
    mess.color('dark blue')
    mess.begin_fill()
    mess.forward(100)
    mess.left(90)
    mess.forward(14)
    mess.left(90)
    mess.forward(70)
    mess.right(90)
    mess.forward(14)
    mess.left(-55)
    mess.forward(42)
    point_1 = mess.position()
    
    mess.right(90-55+180)
    mess.penup()
    mess.forward(63)
    mess.pendown()
    
    mess.left(90)
    mess.forward(51)
    mess.end_fill()
    
    
    mess.color('dark blue')
    mess.begin_fill()
    
    mess.left(180)
    mess.forward(72)
    
#    point_2 = mess.position()
    
    mess.circle(- 20, 90, 50)
    mess.setpos(point_1)
    mess.end_fill() # end M
    
    
    
    mess.penup()
    mess.forward(19.5)
    mess.pendown()
#    point_3 = mess.position()
    
    mess.color('dark blue')
    mess.begin_fill()
    mess.left(140)
    mess.forward(65)
    mess.right(140)
    mess.forward(50)  #edit
    mess.left(90)
#    point_5 = mess.position()
   
    
    
    mess.forward(30)
  
    
    mess.circle(100 / 9, 180, 30)
    mess.forward(10+10)
    mess.right(90)
    mess.forward(20)
    mess.right(90)
    mess.forward(10+10)
    mess.circle(100 / 9, 180, 30)
    mess.forward(23) # 23
    mess.right(90)
    
    mess.circle( 20, 90, 50)
    mess.right(180)
    
    
    mess.forward(50)
    
    mess.circle(-100 / 4, 180, 30)
    mess.right(180)
    mess.circle(-100 / 4, 180, 30)
    
    mess.forward(82)
    mess.circle(- 20, 90, 50)
    mess.left(5)
    mess.forward(33)
    
    mess.right(90+55)
    mess.forward(46)
    mess.end_fill()
     #done
      
mess_logo() 
mess_b1()
mess_b2()


turtle.done()
