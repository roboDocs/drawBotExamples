size(268, 170)

x, y = 26, 44
t = 'abcdefghijk'

fontSize(35)
w, h = textSize(t)
print w, h

# draw the background
fill(1, 0, 0)
rect(x, y, w, h)

# draw the text
fill(0)
text(t, (x, y))
