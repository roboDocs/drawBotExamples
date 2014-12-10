# trigonometry example: analog clock

# get current time
from time import localtime
year, month, day, hours, mins, secs, _, _, _ = localtime()

# define some variables to draw the clock
a_hours = 360 / 12
a_mins = a_secs = 360 / 60
x = width() / 2.0
y = height() / 2.0
s = 812
r = s / 2.0
c = r * 0.15

# draw the base of the clock
stroke(.5)
fill(None)
oval(x-r, y-r, s, s)
line((x, y-c), (x, y+c))
line((x-c, y), (x+c, y))

# draw the marks for minutes/seconds
translate(x, y)
save()
for i in range(60):
    if i % 5 == 0:
        L = r-c
    else:
        L = r-(c/2)
    line((0, L), (0, r))
    rotate(a_secs)
restore()

# draw the seconds
lineCap('round')
stroke(0.2)
save()
strokeWidth(5)
rotate(-secs * a_secs)
line((0, 0), (0, r*0.95))
restore()

# draw the minutes
save()
strokeWidth(12)
rotate(-mins * a_mins)
line((0, 0), (0, r*0.9))
restore()

# draw the hours
save()
strokeWidth(15)
rotate(-hours * a_hours)
line((0, 0), (0, r*0.7))
restore()

