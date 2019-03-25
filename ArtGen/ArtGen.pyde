import random

padik=10
a=500
b=300
x=0


def shtrih():
    background(200)
    for i in range(1):
        x=random.randint(padik,a-padik)
        y=random.randint(1,100)
        h=random.randint(1,100)
        for j in range(3):
            rect(x+j*110,y, h, y)


def setup(): 
    size(a, b)
    frameRate(30)
    strokeWeight(6)
    shtrih()

def draw():
    global x
    x+=1
    if x==20*10:
        x=0
        shtrih()
