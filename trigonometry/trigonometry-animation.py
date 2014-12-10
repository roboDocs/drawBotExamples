# trigonometry circle

from math import sin, cos, radians

# functions

def draw_circle(angle):

    angle_rad = radians(90-angle)
    b = cos(angle_rad)
    c = sin(angle_rad)
    d = w/2.0

    newPage(w, h)
    fill(1)
    rect(0, 0, width(), height())

    translate(w/2.0, h/2.0)

    fill(None)
    strokeWidth(4)
    lineCap('round')

    # stroke(0.7)

    save()
    stroke(0.5)
    strokeWidth(1)
    oval(-a, -a, 2*a, 2*a)
    lineDash(2, 2)
    line((0, -a), (0, a))
    line((-a, 0), (a, 0))
    restore()

    stroke(0, 1, 0)
    line((a*c, 0), (a*c, a*b))
    line((a*c, -d), (a*c, 20-d))
    line((a*c, d), (a*c, -20+d))

    stroke(0.7)
    stroke(0, 0, 1)
    line((0, a*b), (a*c, a*b))
    line((-d, a*b), (20-d, a*b))
    line((d, a*b), (-20+d, a*b))

    stroke(1, 0, 0)
    line((0, 0), (a*c, a*b))

# parameters

w, h = 360, 360
a = 130

# draw!

n = 45
angle_step = 360 / n

for i in range(n):
    draw_circle(-i*angle_step)

saveImage('~/Desktop/trigonometry.gif')
