# recursion example

from progvis.modules.colors import hsv_to_rgb

size(600, 500)
translate(468, 123)
scale(1.4)

n = 87
s = 1.0 / n

while n > 0:
    hue = n * s
    r, g, b = hsv_to_rgb(hue, 1, 1)
    fill(r, g, b, .5)
    rect(-50, -50, 100, 100)
    scale(.93)
    translate(-2, 93)
    rotate(30)
    n -= 1
