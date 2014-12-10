n = 10
drawRectangle = True

while drawRectangle is True:
    print n, 'drawing rectangle...'
    newPage(600, 600)
    rect(0, 0, 100, randint(200, 600))
    n -= 1
    if n == 0:
        drawRectangle = False

print 'drawRectangle is False, stop.'