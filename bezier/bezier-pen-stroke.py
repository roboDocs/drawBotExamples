# draw objects along a bezier segment

def vector((x, y), angle, distance):
    """Calculate a new x,y position based on a given angle and distance."""
    x2 = x + cos(radians(angle)) * distance
    y2 = y + sin(radians(angle)) * distance
    return x2, y2

# converted from:
# http://13thparallel.com/archive/bezier-curves/

def B1(t): return t*t*t
def B2(t): return 3*t*t*(1-t)
def B3(t): return 3*t*(1-t)*(1-t)
def B4(t): return (1-t)*(1-t)*(1-t)

def getPoint(t, (x1, y1), (x2, y2), (x3, y3), (x4, y4)):
    x = x1*B1(t) + x2*B2(t) + x3*B3(t) + x4*B4(t)
    y = y1*B1(t) + y2*B2(t) + y3*B3(t) + y4*B4(t)
    return x, y

size(200, 200)
fill(None)
stroke(1, 0, 0)
strokeWidth(1)

B = BezierPath()
B.moveTo((60, 26))
B.curveTo((-34, 186), (196, 202), (158, 44))
drawPath(B)

p1, p4 = B.onCurvePoints
p2, p3 = B.offCurvePoints

Variable([
    dict(name='n', ui='Slider', args=dict(value=80, minValue=2, maxValue=240)),
    dict(name='a', ui='Slider', args=dict(value=45.0, minValue=0.0, maxValue=180.0)),
    dict(name='f', ui='Slider', args=dict(value=0.5, minValue=0.01, maxValue=1.0)),
    dict(name='edges', ui='CheckBox', args=dict(value=True,)),
],
globals())

n = int(n)
r = 10
w, h = r*2, r*2*f

if edges:
    save()
    x1, y1 = vector(p1, a, w/2)
    d1_x, d1_y = x1 - p1[0], y1 - p1[1]
    translate(d1_x, d1_y)
    drawPath(B)
    restore()

    save()
    x4, y4 = vector(p4, a, w/2)
    d4_x, d4_y = x4 - p4[0], y4 - p4[1]
    translate(-d1_x, -d1_y)
    drawPath(B)
    restore()

for i in range(n+1):
    t = i * (1.0 / n)
    x, y = getPoint(t, p1, p2, p3, p4)
    save()
    translate(x, y)
    rotate(a)
    x, y = -r, -h/2
    oval(x, y, w, h) 
    restore()

