from math import sin, cos, radians

w, h = 600, 600

size(w, h)
translate(w*.5, h*.5)

a = 254
angle = 50

fill(None)
stroke(0.7)
strokeWidth(2)
line((0, -a), (0, a))
line((-a, 0), (a, 0))

stroke(0)
strokeWidth(2)
oval(-a, -a, 2*a, 2*a)

angle_rad = radians(90 - angle)
b = cos(angle_rad)
c = sin(angle_rad)

strokeWidth(2)
stroke(0, 0, 1)
line((a*c, 0), (a*c, a*b))
line((0, a*b), (a*c, a*b))

strokeWidth(3)
stroke(1, 0, 0)
line((0, 0), (a*c, a*b))
