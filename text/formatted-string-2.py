# FormattedString example
# make text fade out, letter by letter

myString = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse mol'

# format the string
myText = FormattedString()
alphaStep = 1.0 / (len(myString) - 1)

for i, char in enumerate(myString):
    # progression from white to black: 1 -> 0
    alpha = 1 - (i * alphaStep)
    color = 0, 0, 1, alpha
    myText.append(char, font='Verdana Bold Italic', fontSize=12, fill=color)

# compose the page with the already formatted string
# check if we have overflow, if so create a new page
while myText:
    newPage(150, 160)
    myText = textBox(myText, (20, 10, width()-30, height()-20))
