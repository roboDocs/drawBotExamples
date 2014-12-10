# clipping path with an image inside

size(518, 398)

# create a bezier path
B = BezierPath()
B.oval(46, 28, 128, 150)
B.oval(80, 176, 294, 158)
B.rect(244, 64, 220, 176)

# draw the bezier path
stroke(1, 0, 0)
strokeWidth(7)
drawPath(B)

# use the path as mask
clipPath(B)

# draw an image inside the path
image("http://gutenberg.org/files/24829/24829-h/images/aldine_virgil.png", (0, 0))
