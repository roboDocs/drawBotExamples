#!/usr/bin/env python
# -*- coding: utf-8 -*-

# a simple font / text example

size(220, 170)

x, y = 30, 110

fill(1, 0, 0)
font("Verdana", 24)
text("hello world", (x, y))

y -= 40

fill(0, 1, 0)
font("Verdana Bold Italic", 24)
text(u"olá mundo", (x, y))

y -= 40

fill(0, 0, 1)
font("Verdana Italic", 24)
text("hola mundo", (x, y))
