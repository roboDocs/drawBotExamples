size(814, 674)

B = BezierPath()
B.text('hi', font='Verdana Bold', fontSize=520, offset=(90, 122))

fill(0, 1, 0)
drawPath(B)

fill(0, 0, 1)
r = 9

for x, y in B.onCurvePoints:
    oval(x-r, y-r, r*2, r*2)
