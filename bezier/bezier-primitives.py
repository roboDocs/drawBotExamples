size(600, 600)

B = BezierPath()
B.oval(44, 68, 200, 200)
B.rect(204, 282, 200, 200)

drawPath(B)

print B.onCurvePoints
print B.offCurvePoints
