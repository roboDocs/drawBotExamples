# [h] animate color range

from progvis.modules.colors import hsv_to_rgb

# functions

def draw_range(steps, factor, start, color_step):
    w = float(width()) / steps
    trap = 1
    hue = start
    x, y = 0, 0
    for i in range(steps):
        r, g, b = hsv_to_rgb(hue, 1, 1)
        fill(r, g, b)
        rect(x-trap, y, w+trap, height())
        hue = (hue + color_step) % 1
        x += w
 
# parameters

steps = 8
factor = 0.25
start = 0

# draw

color_step = (1.00 / steps) * factor

for i in range(steps*4):
    newPage(160, 160)
    draw_range(steps, factor, start, color_step)
    start -= color_step
    start = start % 1

saveImage('~/Desktop/color-range.gif')
