# Variable = vanilla power in DrawBot

Variable([
    # PopUpButton
    {
        'name' : 'aList',
        'ui' : 'PopUpButton',
        'args' : {
            'items' : ['a', 'b', 'c', 'd'],
        }, 
    },
    # EditText
    {
        'name' : 'aText',
        'ui' : 'EditText',
        'args' : { 
            'text' : 'hello world',
        },
    },
    # Slider
    {
        'name' : 'aSlider',
        'ui' : 'Slider',
        'args' : {
            'value' : 100,
            'minValue' : 50,
            'maxValue' : 300
        },
    },
    # CheckBox
    {
        'name' : 'aCheckBox',
        'ui' : 'CheckBox',
    },
    # ColorWell
    {
        'name' : 'aColorWell',
        'ui' : 'ColorWell',
    },
    # RadioGroup
    {
        'name' : 'aRadioGroup',
        'ui' : 'RadioGroup',
        'args' : {
            'titles' : ['I', 'II', 'III'],
            'isVertical' : False,
        },
    },
], globals())

print aList
print aText
print aSlider
print aCheckBox
print aColorWell
print aRadioGroup
