# drawing a bezier path

size(324, 368)

# create bezier path
B = BezierPath()
B.moveTo((36, 52))
B.lineTo((108, 76))
B.curveTo((56, 238), (252, 288), (274, 114))

# draw path
stroke(0, 1, 0)
strokeWidth(5)
fill(None)
drawPath(B)

# draw circles for all points
radius = 10
print B.points
stroke(1, 0, 0)
for x, y in B.points:
    print x, y
    oval(x-radius, y-radius, radius*2, radius*2)
