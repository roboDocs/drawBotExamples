# define a color
c = (1, 0, 0)

# this throws a ValueError!
# fill(c)

# we need to unpack the tuple
fill(*c)

rect(125, 125, 750, 750)
