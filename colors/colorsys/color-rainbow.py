# hsv rainbow

from colorsys import hsv_to_rgb

size(400, 400)

n = 30
w = width()/n

s = 1.0
v = 1.0

color_step = 1.0 / (n-1)

for i in range(n):
    h = i * color_step
    r, g, b = hsv_to_rgb(h, s, v)
    fill(r, g, b)
    stroke(r, g, b)
    rect(0, 0, w, height())
    translate(w, 0)
