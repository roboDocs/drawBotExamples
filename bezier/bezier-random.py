# draw a path through n random points

size(618, 412)

n = 24

B = BezierPath()
for i in range(n):
    # make random point position
    x = randint(0, width())
    y = randint(0, height())
    if i == 0:
        # print 'first point!'
        B.moveTo((x, y))
    else:
        # print 'just another point'
        B.lineTo((x, y))

fill(None)
stroke(1, 0, 0)
strokeWidth(3)
drawPath(B)
