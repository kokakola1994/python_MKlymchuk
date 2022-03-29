from ast import alias
from random import randint
from graphics import *
win = GraphWin("Okno grafiky",1366,1001)
randomlist = []
for i in range(0,1000):
    n = randint(1,1000)
    randomlist.append(n)
for i in range (0,18):
    aLine = Line(Point(randomlist[i],randomlist[i+1]),Point(randomlist[i+2],randomlist[i+3]))
    aLine.setOutline('green')
    if i % 2:
        aLine.draw(win)
aLine2 = Line(Point(randomlist[19],randomlist[20]),Point(randomlist[1],randomlist[2]))
aLine2.setOutline('red')
aLine2.draw(win)
win.getMouse()
win.close()