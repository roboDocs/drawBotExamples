size(302, 344)

def vector(p, d, a):
    x1, y1 = p
    angle_rad = radians(90 - a)
    b = cos(angle_rad)
    c = sin(angle_rad)
    x2 = x1 + (d * c)
    y2 = y1 + (d * b)
    line((x1, y1), (x2, y2))
    return x2, y2

n = 528
a = 71
d = 0.5
L = 2

dashed = False
dashes = [1.7, 1.3]

x, y = 154, 160

lineCap('round')

c = 1.0 / (n - 1)
w = L / (n - 1)

for i in range(n):
    v = L - (i * w)
    if dashed:
        dashes_ = [dash * v for dash in dashes]
        lineDash(dashes_)
    strokeWidth(v)
    cmykStroke(i * c, 0, 1, 0, .5)
    x, y = vector((x, y), d * (i + 1), a * (i + 1))
