# define two points
p1 = 196, 196
p2 = 758, 754

# thick stroke
stroke(0.5)
strokeWidth(170)
lineCap(['round', 'butt', 'square'][2])
line(p1, p2)

# stroke skeleton
stroke(0)
strokeWidth(1)
line(p1, p2)
