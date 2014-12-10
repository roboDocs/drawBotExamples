# grapefruit color schemes

from grapefruit import Color

def draw_swatch(colors, pos, s):
    x, y = pos
    save()
    for c in colors:
        fill(*c)
        rect(x, y, s, s)
        translate(s, 0)
    restore()

c = Color.NewFromHsv(220 % 360, 1, 1) # hue as 360 angle
s = 130
m = s * 0.25
x = y = 120

schemes = [
    (c,) + c.MonochromeScheme(),
    (c,) + c.TriadicScheme(),
    (c,) + c.TetradicScheme(),
    (c,) + c.AnalogousScheme(),
]

for scheme in schemes:
    draw_swatch(scheme, (x, y), s)
    translate(0, s+m)
