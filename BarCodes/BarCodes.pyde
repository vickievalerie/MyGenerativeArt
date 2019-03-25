import random

padik=10
a=500
b=300
x=0


def shtrih():
    background(200)
    for i in range(40):
        x=random.randint(padik,a-padik)
        line(x, padik, x, b-padik)


def setup(): 
    size(a, b)
    frameRate(30)
    strokeWeight(6)
    shtrih()

def draw():
    global x
    x+=1
    if x==30*10:
        x=0
        shtrih()
       
