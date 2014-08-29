#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
http://www.pythonchallenge.com/pc/return/5808.html
'''
# Since May 29 2012

import Image

im = Image.open('cave.jpg')
width, height = im.size

# v1

for y in range(height): # row
    for x in range(width): # column
        if (x+y) % 2 != 0:
            im.putpixel((x,y), (0,0,0))
im.save('cave-replace.jpg')

# v2

im = Image.open('cave.jpg')
newsize = width/2, height/2
im.resize(newsize).save('cave-half.jpg')

# v3

# From http://holger.thoelking.name/python-challenge/11

def putget(oimg, ox, oy, iimg, ix, iy):
    # Calling this looks better
    oimg.putpixel((ox, oy), iimg.getpixel((ix, iy)))

im = Image.open('cave.jpg') # Always let im be the original image
out = [ Image.new(im.mode, newsize) for i in range(4) ]
for y in range(height): # row
    for x in range(width): # column
        if x % 2 == 0 and y % 2 == 0:
            putget(out[0], x/2, y/2, im, x, y)
        elif x % 2 == 0 and y % 2 == 1:
            putget(out[1], x/2, (y-1)/2, im, x, y)
        elif x % 2 == 1 and y % 2 == 0:
            putget(out[2], (x-1)/2, y/2, im, x, y)
        else:
            putget(out[3], (x-1)/2, (y-1)/2, im, x, y)

for image in out:
    image.save('cave%d.jpg' % out.index(image))

# v4

# v3 improved
im = Image.open('cave.jpg') # Always let im be the original image
out = [ Image.new(im.mode, newsize) for i in range(4) ]
for y in range(height): # row
    for x in range(width): # column
        rx, ry = x % 2, y % 2
        putget(out[(rx<<1)+ry], (x-rx)/2, (y-ry)/2, im, x, y)

for image in out:
    image.save('cave%d.jpg' % (out.index(image)+4))
