# composition with triangles
# homage to Anni Albers

# parameters

w, h = 10, 10
x, y = 0, 0
a = 50
r = a / 2.0

c1 = 1, 0 , 0
c2 = 0, 0, 1

# draw!

size(w*a, h*a)
fill(*c1)
rect(0, 0, width(), height())
fill(*c2)

for i in range(h):
    for j in range(w):
        save()
        # translate to rotation center
        translate(x+r, y+r)
        # random rotation
        R = random()
        if R < .25:
            rotate(90)
        elif .25 < R < .5:
            rotate(180)
        elif .5 < R < .75:
            rotate(270)
        else:
            rotate(360)
        # draw triangle
        newPath()
        moveTo((0-r, 0-r))
        lineTo((r, 0-r))
        lineTo((0-r, r))
        closePath()
        drawPath()
        restore()
        # shift x
        x += a
    # shift y
    x = 0
    y += a
