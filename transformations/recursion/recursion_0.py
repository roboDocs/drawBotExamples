n = 20
scale(3.0)

while n > 0:
    r = 1.0 / n
    fill(r, 0, 0, 0.5)
    rect(0, 0, 100, 100)
    translate(15, 78)
    scale(0.85)
    rotate(-17)
    n -= 1
