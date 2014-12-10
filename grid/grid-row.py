# draw a row of rectangles

n = 8
w, h = 100, 400

for i in range(n):
    fill(random(), random(), random())
    x = i * w
    rect(x, 0, w, h)
