# homenagem ao Hans Donner

from AppKit import NSColor

x = width() / 2
y = height() / 2
r = 408
rw = r * .7
rh = r * .51
r2 = r * .4

c2 = (0, 1, 1)
c3 = (1, 1, 0)

var_1 = {
    'name': "c1",
    'ui': "ColorWell",
    'args': {
        'color': NSColor.colorWithCalibratedRed_green_blue_alpha_(.3, .4, 1, .8),
    }
}

Variable([var_1], globals())

fill(c1)
oval(x - r, y - r, r * 2, r * 2)

linearGradient(
    (x, y - rh),  # start
    (x, y + rh),  # end
    [c2, c3, ],   # colors
    [0.0, 1.0],   # positions
)

rect(x - rw, y - rh, rw * 2, rh * 2)

fill(c1)
oval(x - r2, y - r2, r2 * 2, r2 * 2)
