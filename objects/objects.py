from drawBot import *

class Rectangle:
    
    fillColor = (0, 1, 0)
    strokeColor = (0, 0, 1)
    strokeWidth = 3

    def __init__(self, size=None):
        if size is not None:
            w, h = size
            self.width = w 
            self.height = h
        else:
            self.width = 200
            self.height = 200

    def draw(self, (x, y)):
        save()
        fill(*self.fillColor)
        stroke(*self.strokeColor)
        strokeWidth(self.strokeWidth)
        rect(x, y, self.width, self.height)
        restore()
