# grapefruit gradient example

from grapefruit import Color

size(300, 300)

c1 = Color.NewFromHsv(225, 1, 1)
c2 = Color.NewFromHsv(65, 1, 1)

steps = 20
s = width() / float(steps)

gradient = [c1]
gradient += c1.Gradient(c2, steps)
gradient += [c2]

for c in gradient:
    fill(*c)
    stroke(*c)
    rect(0, 0, s, height())
    translate(s, 0)
