help(image)

# a local png image with transparent background
img_1 = u"monty_python_foot.png"

# a jpeg image from the web
img_2 = 'http://patcomputerizedworld.files.wordpress.com/2014/03/guido-van-rossum_python.jpg'

image(img_2, (0, 0))

# optional 3rd argument: transparency
image(img_2, (200, 100), 0.5)

scale(2)
image(img_1, (10, 180))
