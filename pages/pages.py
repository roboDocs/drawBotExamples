# creating pages

w, h = 200, 200
n = 20

for i in range(n):
    newPage(w, h)
    fill(random(), random(), random())
    rect(0, 0, width(), height())
    fill(0)
    text(str(i+1), (20, 20))

print pageCount()
