# size of squares/circles
s = 294

# draw black square
rect(170, 474, s, s)

# draw transparent oval
fill(.5, .5)
oval(184, 68, s, s)

# draw square with green stroke
stroke(0, 1, 0)
strokeWidth(32)
rect(362, 572, s, s)

# draw dashed red line
stroke(1, 0, 0)
# lineCap('round')
lineDash(50, 39)
line((54, 36), (878, 626))

# draw triangle with blue rounded stroke
stroke(0, 0, 1)
lineDash(None)
lineJoin('round')
polygon((556, 140), (850, 454), (863, 116))
