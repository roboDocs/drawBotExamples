# basic typesetting

size(600, 600)

myText = """Draws text to the screen. The first parameter sets the string of text to display ("always between quotes"). The following two parameters set the location of the text's baseline. The fourth, fifth and sixth parameter are optional. The fourth parameter specifies a width for text blocks, the fifth the maximum height. Text in a block is wrapped across multiple lines. The alignment for text in a block can be set with the align() command. By default, text is not outlined when saved as a PDF. Optionally, a sixth parameter outline=True can be supplied so text will be outlined."""

# define current font and size
font('Andale Mono', 16)

# lineHeight not documented (skip lineheight, lowercase deprecated)
lineHeight(20)

# define textbox and alignment (it's a keyword argument)
textBox(myText, (50, 50, 400, 400), align='left')

# some useful helper functions:
# get the size of a text as tuple (width, height)
print textSize(myText, align='left')

# get a list of installed fonts
# print installedFonts()
