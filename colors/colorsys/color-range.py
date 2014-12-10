# color range with sliders

from colorsys import hsv_to_rgb

# parameters

slider_1 = {
    'name' : 'steps',
    'ui' : 'Slider',
    'args' : {
        'value' : 11, 
        'minValue' : 3, 
        'maxValue' : 100,            
        }
    }

slider_2 = {
    'name' : 'color_factor',
    'ui' : 'Slider',
    'args' : {
        'value' : .1, 
        'minValue' : .01, 
        'maxValue' : 2.4,            
        }
    }

slider_3 = {
    'name' : 'color_start',
    'ui' : 'Slider',
    'args' : {
        'value' : .1, 
        'minValue' : 0, 
        'maxValue' : 1.0,            
        }
    }

Variable([slider_1, slider_2, slider_3], globals())

# draw

size(800, 600)

steps = int(steps)
color_step = (1.00 / steps) * color_factor
width = float(width()) / steps
trap = 1
hue = color_start

x, y = 0, 0

for i in range(steps):
    r, g, b = hsv_to_rgb(hue, 1, 1)
    fill(r, g, b)
    rect(x - trap, y, width + trap, height())
    hue = (hue + color_step) % 1
    x += width
 