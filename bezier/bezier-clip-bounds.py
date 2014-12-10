size(300, 200)

x = 20
B = BezierPath()
for i in range(8):
    B.oval(x, 68, 40, 70)
    x += 25

save()
clipPath(B)
scale(0.5)
image("https://i.ytimg.com/vi/JfIgzSoTMOs/hqdefault.jpg", (0, 0))
restore()

# print B.onCurvePoints
# print B.offCurvePoints

x, y, w, h = B.bounds()

fill(None)
stroke(0, 1, 0)
rect(x, y, w, h)
