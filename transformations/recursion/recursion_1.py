# recursion example

size(400, 500)
translate(136, 107)
scale(1.4)

n = 12
s = 1.0 / n

while n > 0:
    fill(n * s, 0, 0, .6)
    rect(-50, -50, 100, 100)
    scale(.80)
    translate(58, 72)
    rotate(45)
    n -= 1
