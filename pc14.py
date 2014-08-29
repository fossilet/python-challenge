#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
http://www.pythonchallenge.com/pc/return/italy.html
'''
# Since May 31 2012

import Image

im = Image.open('wire.png')
data = list(im.getdata())
nim = Image.new(im.mode, (100, 100))

# Wrong curve
nim.putdata(data)
nim.save('wire1.png')


# TODO: not finished
def get_coor(ind):
    '''ind is the index of the data in the 10000x1 stripe.
    Returns the coordinate of the pixel in the new 100x100 image.
    '''
    return (0, 0)


def get_box(data):
    '''For data list, returns the box in which is the pixel.
    '''
    #for ind in range(len(data)):
    #coor = get_coor(ind)
    for box_size in range(100, 0, -2):
        print box_size
        if box_size == 2:
            return 'Is in the %sx%s box.' % (box_size, box_size)
        else:
            return get_box(data[4 * box_size:])

print get_box(data)


# Right curve
    #nim.putpixel(coor, data[ind])
nim.save('wire2.png')
