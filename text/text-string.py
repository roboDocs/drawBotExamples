# get a list of all installed fonts
# print installedFonts()

font('ComicSansMS-Bold')
fontSize(140)

# draw some text
text('hello world', (134, 620))

translate(0, -200)

n = 36789

# this will throw an error!
# text(n, (134, 620))

# always convert other data types to string
text(str(n), (134, 620))
