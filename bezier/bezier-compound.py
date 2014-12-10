size(100, 100)

# create a Bezier object
B = BezierPath()

# create first contour
B.moveTo((10, 10))
B.lineTo((26, 48))
B.lineTo((20, 72))
B.curveTo((44, 92), (94, 94), (70, 24))
B.closePath()

# create second contour (from points list)

# define a list of points
points = [(30, 24), (62, 34), (44, 66)]

# move to first point
x, y = points[0]
B.moveTo((x, y))
# make straight segments with other points
for point in points[1:]:
    B.lineTo(point)
B.closePath()

# draw the path
stroke(1, 0, 0)
fill(0, 1, 0)
drawPath(B)

# some path methods
# print B.points
# print B.onCurvePoints
# print B.offCurvePoints
