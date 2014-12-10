from colorsys import hsv_to_rgb

h, s, v = 0.5, 1.0, 1.0
r, g, b = hsv_to_rgb(h, s, v)

fill(r, g, b)
rect(0, 0, width(), height())
