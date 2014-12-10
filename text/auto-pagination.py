#!/usr/bin/env python
# -*- coding: utf-8 -*-

T = u"""There was a day when designers asked themselves: ‘Why use a computer for design?’. Some argued that a computer was not needed for being a good designer. The important thing was the designer himself/herself. They were right.
Some years later and there is hardly any designer working without a computer. The computer has become the designer’s main tool (sometimes even the only one nowadays).
Software is developed mainly by engineers, not by designers. This makes the designer constrained by the engineers’ thoughts and ideas, not by his/her own. Programming gives the designer more control over his/her tools, and therefore over the design process. It allows one to follow the own workflow and think beyond the resources included in the software.
Probably you don’t need to know how to program to be a better designer. But it might help. And it won’t hurt, for sure."""

x, y = 94, 282
w, h = 800, 600

i = 0
while len(T) > 0:
    newPage(1000, 1000)
    if i % 2 == 0:
        fontSize(60)
        font('Times-Bold')
        fill(1, 0, 0)
        a = 'left'
    else:
        fontSize(52)
        font('Verdana-Bold')
        fill(0, 1, 0)
        a = 'right'
    hyphenation(False)
    lineHeight(70)
    T = textBox(T, (x, y, w, h), align=a)
    text(str(i+1), (66, 42))
    i += 1
