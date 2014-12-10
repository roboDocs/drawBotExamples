# use division rest to cycle through colors

x, y = 0, 0
w, h = 20, 15
module = 20

# make colors
colors_amount = randint(5, 19)
colors = [(random(), random(), random()) for i in range(colors_amount)]

size(w*module, h*module)

# draw modules
count = 0
for i in range(h):
    save()
    for j in range(w):
        index = count % colors_amount
        color = colors[index]
        fill(*color)
        rect(0, 0, module, module)
        translate(module, 0)
        count += 1
    restore()
    translate(0, module)
