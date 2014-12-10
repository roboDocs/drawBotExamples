size(600, 600)

# set line properties
fill(None)
strokeWidth(33)
stroke(1, 0, 0)
lineCap('butt')  # round, butt, square
lineJoin('miter')  # round, miter, bevel
miterLimit(2)
# lineDash(6, 5)

# create a new path
newPath()

# define the path segments
moveTo((92, 38))
lineTo((381, 155))
lineTo((130, 375))
lineTo((96, 142))
lineTo((320, 291))
curveTo((5, 534), (579, 708), (425, 259))

# draw the path to the canvas
drawPath()
