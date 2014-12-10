# testing frames with different duration values

for i in range(20):
    newPage(100, 100)
    frameDuration(0.1 * (i+1))
    fill(random(), random(), random())
    rect(0, 0, width(), height())

saveImage('teste.mov', multipage=False)
