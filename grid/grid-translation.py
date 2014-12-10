# grid (using translation)

w, h = 8, 10
s = 20

size(w*s, h*s)

for i in range(w):
    save()
    for j in range(h):
        fill(random())
        rect(0, 0, s, s)
        translate(0, s)
    restore()
    translate(s, 0)
