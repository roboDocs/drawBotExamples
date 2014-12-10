# getting the center of a rectangle

w, h = 341, 379
x, y = 135, 59
L = 23

size(600, 600)

rect(x, y, w, h)

center_x = x + (w / 2.0)
center_y = y + (h / 2.0)

strokeWidth(2)
stroke(1, 0, 0)
line((center_x, center_y - L), (center_x, center_y + L))
line((center_x - L, center_y), (center_x + L, center_y))
