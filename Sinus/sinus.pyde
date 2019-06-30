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
nsin=5

d=[]

def draw():
    global x,d
    if x%10 == 0:
        background(255)
        for i in d:
            drawsin(i[0],i[1],i[2],i[3],i[4],i[5])
        if len(d)==nsin:
            d=d[1:]
        d.append([random.randint(50,200),random.randint(5,20),random.randint(100,800),random.randint(5,25),random.randint(30,100),random.randint(1,5)])
        
    x+=1




    
    
