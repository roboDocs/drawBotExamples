# get n random fonts from the system

translate(100, 100)
n = 7
for i in range(n):
    f = choice(installedFonts())
    print f
    font(f, 81)
    text('handgloves', (0, 0))
    translate(0, 100)