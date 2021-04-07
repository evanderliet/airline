# entry.py

from graphics import *

class textEntry_():
    def __init__(self, win, center, text):
        Text(center, text).draw(win)
        p1 = Point(center.getX() + 10, center.getY())
        self.input = Entry(p1, 12)
        self.input.setText("")
        self.input.fill = "white"
        self.input.draw(win)
        