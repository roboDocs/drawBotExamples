from AppKit import NSColor

var_1 = {
    'name': "c1",
    'ui': "ColorWell",
    'args': {
        'color': NSColor.colorWithCalibratedRed_green_blue_alpha_(.3, .4, 1, .8),
    }
}

Variable([var_1], globals())

size(300, 300)

# passing the color to `fill`
fill(c1) # look ma, no tuple unpacking!
oval(20, 20, 220, 220)

linearGradient(
    (30, 176),
    (0, width()),
    # passing the color to `gradient`
    [c1, (0,)],
    [0.0, 0.6],
)

oval(166, 158, 120, 120)
