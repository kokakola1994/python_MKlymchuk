from random import choice, randint
from time import sleep
from graphics import *
win = GraphWin("Okno grafiky",1366,1001)
ryb = ['red','yellow','blue']
ryb1 = ['green','gray','black']
randColor=choice(ryb)
randColor1=choice(ryb1)
anOval = Oval(Point(300,300), Point(500,500))
centerPoint = anOval.getCenter()
cornerPoint = anOval.getP1()
anOval.setOutline('green')
anOval.setWidth(5)
anOval.draw(win)
aRectangle = Rectangle(Point(600,600), Point(700,700))
centerPoint = aRectangle.getCenter()
cornerPoint = aRectangle.getP1()
aRectangle.setOutline('red')
aRectangle.setWidth(5)
aRectangle.draw(win)
for i in range(100,750):
    c = Circle(Point(100,100),30)
    c.setOutline(randColor)
    c.setWidth(5)
    c.setFill(randColor1)
    c.move(i,i)
    sleep(0.01)
    c.draw(win)
win.getMouse()
win.close()