size(200, 200)

# make a bezier path
B = BezierPath()
B.moveTo((24, 168))
B.lineTo((14, 24))
B.lineTo((176, 28))
B.lineTo((136, 170))

# draw the bezier path
strokeWidth(5)
fill(None)
stroke(1, 0, 0)
drawPath(B)

# make a grid of elements
# draw them only inside the bezier

stroke(0, 1, 0)
strokeWidth(3)
x, y = 0, 0
dist = 15

for x in range(0, width(), dist):
    for y in range(0, height(), dist):
        if B.pointInside((x, y)):
            r = randint(3, 8)
            oval(x-r, y-r, r*2, r*2)

# change the path's point coordinates
# watch how the bubbles follow the shape
