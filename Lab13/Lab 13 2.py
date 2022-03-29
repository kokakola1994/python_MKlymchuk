from graphics import *
from random import choice, randint
win = GraphWin("Okno grafiky",1366,1001)
win.setBackground("lightgreen")
for i in range(0,1001):
        randNumx=randint(0,1000)
        randNumy=randint(0,1000)
        ryb = ['red','yellow','blue']
        randColor=choice(ryb)
        pt=Point(randNumx,randNumy)
        pt.setOutline(randColor)
        pt.draw(win)
win.getMouse()
win.close()