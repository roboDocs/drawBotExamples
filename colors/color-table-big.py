# RGB color table 
# based on http://en.wikipedia.org/wiki/File:1Mcolors.png

def draw_square(steps, pos, b):
    color_step = 1.0 / steps
    x, y = pos
    for i in range(steps):
        for j in range(steps):
            r = j * color_step
            g = i * color_step
            fill(r, g, b)
            stroke(r, g, b)
            strokeWidth(0.1)
            rect(x, y, 1, 1)
            x += 1
        x = pos[0]
        y += 1

def draw_table(steps, pos):
    x, y = pos
    b = 0
    count = 0
    color_step = 1.0 / (steps[0] ** 2)
    for i in range(steps[0]):
        for j in range(steps[0]):
            draw_square(steps[1], (x, y), b)
            b = count * color_step
            x += steps[1]
            count += 1
        x = pos[0]
        y += steps[1]

steps = 4, 10
s = steps[0] * steps[1]
size(s, s)
draw_table(steps, (0, 0))
