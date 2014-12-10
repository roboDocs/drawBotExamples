# create a list of colors
colors = [
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 1, 1),
    (0, 0, 1),
    (1, 0, 1),
]

# randomly choose a color from the list
color = choice(colors)
print color

# draw a square with this color
fill(*color)
rect(0, 0, width(), height())
