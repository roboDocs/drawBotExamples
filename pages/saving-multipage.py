# testing multipage options

for i in range(6):
    newPage(200, 200)
    fill(random(), random(), random())
    rect(0, 0, width(), height())

    # default
    saveImage(['test_0.pdf', 'test_0.png'])
    # multi-page pdf / last page as png

    # multipage False, inside loop
    saveImage(['test_1.pdf', 'test_1.png'], multipage=False)
    # last page as pdf / last page as png

    # multipage True, inside loop
    saveImage(['test_2.pdf', 'test_2.png'], multipage=True)
    # multi-page pdf / all pages as png, numbers added

# default
saveImage(['test_3.pdf', 'test_3.png'])
# multi-page pdf / last page as png

# multipage False
saveImage(['test_4.pdf', 'test_4.png'], multipage=False)
# last page as pdf / last page as png

# multipage True
saveImage(['test_5.pdf', 'test_5.png'], multipage=True)
# multi-page pdf / all pages as png, numbers added
