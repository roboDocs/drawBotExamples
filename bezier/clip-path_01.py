# clipping path example

# draw a grid of rectangles
B = BezierPath()
for x in range(0, width(), 100):
    for y in range(0, height(), 100):
        B.rect(x, y, 80, 80)

# draw the grid path
fill(0, 1, 0)
drawPath(B)

# save before entering clipping mode
save()
clipPath(B)

# draw yellow rectangle inside grid
rotate(20)
fill(1, 1, 0)
stroke(None)
rect(396, -50, 600, 600)

# exit clipping mode
restore()

# draw blue circle on top of grid
fill(0, 0, 1)
stroke(None)
oval(244, 240, 200, 200)
