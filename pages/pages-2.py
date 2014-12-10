# creating pages (with random sizes)

n = 20

for i in range(n):
    w, h = randint(140, 200), randint(140, 200)
    newPage(w, h)
    fill(random(), random(), random())
    rect(0, 0, width(), height())
    fill(0)
    text(str(i+1), (20, 20))

print pageCount()
