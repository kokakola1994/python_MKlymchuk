from random import choice
from graphics import *
from time import sleep
win = GraphWin("Okno grafiky",1366,1001)
ryb = ['red','yellow','blue']
ryb1 = ['green','gray','black']
randColor=choice(ryb)
randColor1=choice(ryb1)
c = Circle(Point(100,100),30)
c.setOutline(randColor)
c.setWidth(5)
c.setFill(randColor1)
sleep(0.01)
c.draw(win)
dx, dy = 10, 0
dx1, dy1 = 0, 10
while True:
    k = win.checkKey()
    if k == 'a':
        c.move(-dx, dy)
    elif k == 'd':
        c.move(dx, dy)
    elif k == 'w':
        c.move(dx1, -dy1)
    elif k == 's':
        c.move(dx1, dy1)
    elif k == 'q':
        break

win.close()