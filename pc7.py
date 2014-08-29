#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
http://www.pythonchallenge.com/pc/def/oxygen.html
'''
# Since May 25 2012
# Depends on PIL

import Image

im = Image.open('oxygen.png')
width = im.size[0]
step = 7
row =  (im.getpixel((i, 50)) for i in range(0, width, step))
msg = ''.join(chr(r) for (r, g, b, a) in row if r == g == b)
print msg
print ''.join(chr(c) for c in eval(msg[msg.find('['):]))
