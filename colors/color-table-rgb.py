size(200, 200)

w, h = 10, 10
x, y = 24, 18
s = 15

colorstep_r = 1.0 / (h-1)
colorstep_g = 1.0 / (w-1)
b = 0.5

for j in range(w):
    for i in range(h):
        g = j * colorstep_g
        r = i * colorstep_r
        fill(r, g, b)
        stroke(r, g, b)
        rect(x, y, s, s)
        translate(0, s)
    translate(s, -(s*h))
