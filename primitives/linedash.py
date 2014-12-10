size(200, 200)

# print help(lineDash)

lineCap('butt')
stroke(1, 0, 0)
strokeWidth(3)

lineDash(5, 2, 2, 5)
line((20, 20), (164, 170))

stroke(0, 1, 0)
lineDash(8, 3)
line((124, 20), (180, 150))