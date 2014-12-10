# simple diameter/radius example
# drawing a circle from center

x, y = 462, 488
diameter = 560
radius = diameter * 0.5
stroke_width = 5

# draw the circle's start position
stroke(0, 1, 0)
strokeWidth(stroke_width)
line((x-radius, 0), (x-radius, height()))
line((0, y-radius), (width(), y-radius))

# draw the circle
fill(0)
stroke(None)
oval(x-radius, y-radius, diameter, diameter)

# draw the circle's center (x,y)
stroke(1, 0, 0)
strokeWidth(stroke_width)
line((x, 0), (x, height()))
line((0, y), (width(), y))
