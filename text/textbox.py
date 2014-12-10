size(200, 200)

p = 'Some operations are supported by several object types; in particular, practically all objects can be compared, tested for truth value, and converted to a string (with the repr() function or the slightly different str() function). The latter function is implicitly used when an object is written by the print() function.'

x, y = 10, 20
w, h = 134, 142

hyphenation(True)
textBox(p, (x, y, w, h), 'right')
strokeWidth(4)
stroke(1, 0, 0)
fill(None)
rect(x, y, w, h)
