size(800, 600)

# make a FormattedString object
txt = FormattedString()

# add some text with formatting
txt.append("hello", font="Helvetica", fontSize=100, fill=(1, 0, 0))

# add some more text with another formatting
txt.append("world", font="Times-Italic", fontSize=115, fill=(0, 1, 0))

# draw the FormattedString on canvas
text(txt, (120, 300))
