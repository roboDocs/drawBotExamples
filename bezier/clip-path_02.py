# path clipping example

size(800, 600)
fill(None)
strokeWidth(3)

# create and draw a path
B = BezierPath()
B.moveTo((220, 72))
B.curveTo((-213, 590), (881, 700), (573, 117))
drawPath(B)

# draw some random bubbles
for a in range(100):
    x = randint(0, width())
    y = randint(0, height())
    sz = randint(10, 50)
    stroke(random(), .2)
    oval(x, y, sz, sz)

# enter clipping mode, draw some colourful stripes
clipPath(B)

w = 20
steps = int(width() / w)
stroke(None)

for i in range(steps):
    fill(random(), random(), random())
    rect(i * w, 0, w, height())
