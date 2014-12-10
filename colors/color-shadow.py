# color shadow example

size(600, 600)

# save the current state
save()

# apply the shadow
shadow((17, -15), 20, (1, 0, 0))

# draw some objects
rect(94, 230, 178, 184)

font('Verdana Bold')
fontSize(70)
text('hello', (100, 100))

# disable the shadow
restore()

# draw something (no shadow)
oval(366, 318, 150, 150)
