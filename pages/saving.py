# number of pages
n = 5

for i in range(n):
    # create new page
    newPage(500, 500)
    # define graphic state
    fill(1, 0, 0)
    # draw a random rect
    rect(0, 0, randint(20, 400), randint(20, 400))
    # save every image, use string formatting
    saveImage([
        u'output_%s.png' % (i + 1),
        u'output.jpg',
    ])
    
# save multipage pdf and movie out of the loop
saveImage([
    u'output.pdf',
    u'output.mov',
])
