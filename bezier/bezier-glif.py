# draw a .glif using the BezierPath object

from robofab.world import RFont

# path to any ufo file
ufo = u"/Users/gferreira/Desktop/Publica_55.ufo"

# open the font, get a glyph
font = RFont(ufo)
glyph = font['a']

B = BezierPath()
for contour in glyph:
    for i, segment in enumerate(contour):
        # curveTo
        if len(segment.points) == 3:
            x1, y1 = segment.points[0].x, segment.points[0].y
            x2, y2 = segment.points[1].x, segment.points[1].y
            x3, y3 = segment.points[2].x, segment.points[2].y
            B.curveTo((x1, y1), (x2, y2), (x3, y3))
        # lineTo or moveTo
        else:
            x, y = segment.points[0].x, segment.points[0].y
            if i == 0:
                B.moveTo((x, y))
            else:
                B.lineTo((x, y))

translate(142, 168)
drawPath(B)
