# simple vector example
# a line with starting point, length and angle

def vector(pos, length, angle):
    x1, y1 = pos
    angle_rad = radians(90-angle)
    b = cos(angle_rad)
    c = sin(angle_rad)
    x2 = x1 + (length*c)
    y2 = y1 + (length*b)
    line((x1, y1), (x2, y2))

size(302, 344)

L = 174
a = 65

strokeWidth(13)
stroke(0, 0, 1)
lineCap('round')

vector((96, 74), L, a)
