#!/usr/bin/env python
# -*- coding: utf-8 -*-

fontSize(35)
hyphenation(True)

# textBox returns the text which did not fit into the box
print textBox(u'''There was a day when designers asked themselves: ‘Why use a computer for design?’. Some argued that a computer was not needed for being a good designer. The important thing was the designer himself/herself. They were right.
Some years later and there is hardly any designer working without a computer. The computer has become the designer’s main tool (sometimes even the only one nowadays).
Software is developed mainly by engineers, not by designers. This makes the designer constrained by the engineers’ thoughts and ideas, not by his/her own. Programming gives the designer more control over his/her tools, and therefore over the design process. It allows one to follow the own workflow and think beyond the resources included in the software.
Probably you don’t need to know how to program to be a better designer. But it might help. And it won’t hurt, for sure.''', (80, 110, 600, 700))
