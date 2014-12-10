# set stroke properties
stroke(1, 0, 0)
strokeWidth(112)

# 'round', 'square', 'butt'
lineCap('round')

# 'round', 'bevel', 'miter'
miterLimit(2)
lineJoin('miter')

# draw a bezier
newPath()
moveTo((128, 150))
lineTo((316, 718))
lineTo((748, 264))
# closePath()
drawPath()
