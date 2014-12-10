# grid (using a function)

def draw_col(h):
    for i in range(h):
        c = random(),
        fill(*c)
        rect(0, 0, s, s)
        translate(0, s)

w, h = 8, 10
s = 20

size(w*s, h*s)

for j in range(w):
    draw_col(h)
    translate(s, -(s*h))
