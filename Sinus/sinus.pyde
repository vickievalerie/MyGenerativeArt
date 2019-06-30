import math
import random

def setup():
    rectMode(CENTER)
    background(255)
    fill(127)
    size(1024,1024)
#    rect(100,100,150,150)
#    for i in range(20):
#        rect(i*60,sin(i)*100+150,30,90)
#    drawsin(100,10,100,10,60,5)

    drawsin(random.randint(50,200),random.randint(5,20),random.randint(100,800),random.randint(5,25),random.randint(30,100),random.randint(1,5))
    
def drawsin(h,w,y,wkv,hkv,ng):
    nkv=width/(wkv+w)
    for i in range(nkv):
        rect(i*(wkv+w),sin(myscale(i,0.0,nkv,0,2*ng*math.pi))*h+y+h/2,wkv,hkv)
        
def myscale(x,a1,b1,a2,b2):
    t=(x-a1)/(b1-a1)
    return t*(b2-a2)+a2

x=0
app=[random.randint(50,200),random.randint(5,20),random.randint(100,800),random.randint(5,25),random.randint(30,100),random.randint(1,5)]
ap=[random.randint(50,200),random.randint(5,20),random.randint(100,800),random.randint(5,25),random.randint(30,100),random.randint(1,5)]
a=[random.randint(50,200),random.randint(5,20),random.randint(100,800),random.randint(5,25),random.randint(30,100),random.randint(1,5)]

def draw():
    global x,app,ap,a
    if x%120 == 0:
        background(255)
        drawsin(app[0],app[1],app[2],app[3],app[4],app[5])
        drawsin(ap[0],ap[1],ap[2],ap[3],ap[4],ap[5])
        drawsin(a[0],a[1],a[2],a[3],a[4],a[5])
        app=ap
        ap=a
        a=[random.randint(50,200),random.randint(5,20),random.randint(100,800),random.randint(5,25),random.randint(30,100),random.randint(1,5)]
    x+=1




    
    
