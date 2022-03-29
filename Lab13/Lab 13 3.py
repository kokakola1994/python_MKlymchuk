from random import choice, randint
from time import sleep
from graphics import *
win = GraphWin("Okno grafiky",1366,1001)
for i in range(0,51):
    sleep(0.1)
    randNumx=randint(0,1000)
    randNumy=randint(0,1000)
    randNumr=randint(10,30)
    ryb = ['red','yellow','blue']
    ryb1 = ['green','gray','black']
    randColor=choice(ryb)
    randColor1=choice(ryb1)
    c = Circle(Point(randNumx,randNumy),randNumr)
    c.setOutline(randColor)
    c.setWidth(5)
    c.setFill(randColor1)
    c.draw(win)
win.getMouse()
win.close()