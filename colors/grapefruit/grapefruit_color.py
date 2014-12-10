# grapefruit example

from grapefruit import Color

size(400, 400)

# create a color from RGB values
c = Color.NewFromRgb(1, 0, 0)

# convert color to other modes
print 'hsv: %s %s %s' % c.hsv
print 'hsl: %s %s %s' % c.hsl
print 'lab: %s %s %s' % c.lab
print 'cmyk: %s %s %s %s' % c.cmyk

r = 125

fill(*c)
rect(20, 20, r, r)

# complementary color
fill(*c.ComplementaryColor())
rect(60, 70, r, r)

# new color from HSV values
fill(*Color.NewFromHsv(30, 1, 1))
rect(220, 220, r, r)

# new color from hex value
fill(*Color.NewFromHtml('#07F'))
rect(220, 70, r, r)

