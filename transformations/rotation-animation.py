# parameters

d = 70
n = 3
a = 1

# draw!

r = d / 2.0
steps = int(90/a)

for p in range(1, steps+1):
    newPage(n*d, n*d)
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    for i in range(n):
        for j in range(n):
            x, y = i*d, j*d
            save()
            translate(x+r, y+r)
            rotate(p*(i+1)*(j+1)*a)
            scale(0.7)
            rect(-r, -r, d, d)
            restore()
            
# saveImage('~/Desktop/rotations.gif')
