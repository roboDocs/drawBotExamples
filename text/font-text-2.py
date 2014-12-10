size(200, 200)

t = '''Solarized is a sixteen color palette (eight monotones, eight accent colors) designed for use with terminal and gui applications. It has several unique properties. I designed this colorscheme with both precise CIELAB lightness relationships and a refined set of hues based on fixed color wheel relationships. It has been tested extensively in real world use on color calibrated displays (as well as uncalibrated/intentionally miscalibrated displays) and in a variety of lighting conditions.'''

# print installedFonts()

fill(1, 0, 0)
fontSize(50)
font('GillSans-Italic')
lineHeight(40)
text('hello\nworld', (30, 22))

fill(0, 1, 0)
fontSize(9)
lineHeight(9)
r = textBox(t, (69, 57, 106, 118), align='right')
print r