size(300, 300)

stroke(0, 1, 0)
strokeWidth(9)
fill(None)

B = BezierPath()
B.moveTo((30, 38))
B.lineTo((250, 44))
B.curveTo((234, 202), (90, 384), (52, 94))
drawPath(B)

print B.points
print B.onCurvePoints
print B.offCurvePoints

x, y = 154, 136
fill(1, 0, 0)
stroke(None)
oval(x-15, y-15, 30, 30)

print B.pointInside((x, y))
