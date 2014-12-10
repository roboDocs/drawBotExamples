# grid (using position)

x, y = 0, 0
w, h = 8, 10
s = 20

size(w*s, h*s)

for j in range(w):
    for i in range(h):
        c = random(),
        fill(*c)
        rect(x, y, s, s)
        y += s
    y -= s * h
    x += s
