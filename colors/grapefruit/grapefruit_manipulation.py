# grapefruit color manipulation

from grapefruit import Color

size(300, 300)

manipulations = [
    'Desaturate',
    'Saturate',
    'LighterColor',
    'DarkerColor',
]

color = Color.NewFromHsv(175 % 360, 0.5, 0.5)
steps = 15
factor = 0.025

s = width() / float(steps)
h = height() / float(len(manipulations))

for m in manipulations:
    save()
    for i in range(steps):
        exec 'c = color.%s(i*factor)' % m
        fill(*c)
        stroke(*c)
        rect(0, 0, s, height())
        translate(s, 0)
    restore()    
    translate(0, h)
