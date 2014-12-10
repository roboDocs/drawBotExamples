size(500, 500)

# define image paths
images = [
    'https://www.fontfont.com/staticcontent/designerimages/original/2807.jpg',
    'https://0.academia-photos.com/1538038/543949/679382/s200_erik.van_blokland.jpg'
]

# choose one image randomly
img = choice(images)

# draw image
x, y = 100, 100
image(img, (x, y))

# get width & height of image
w, h = imageSize(img)

# draw frame around web image
stroke(0, 1, 0)
strokeWidth(10)
fill(None)
rect(x, y, w, h)
