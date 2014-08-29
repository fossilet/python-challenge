#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
http://www.pythonchallenge.com/pc/return/good.html
'''
# Since May 29 2012

from matplotlib.pyplot import plot, show

fds = open('pc9-text1'), open('pc9-text2')
points = [ eval('[%s]' % fd.read()) for fd in fds ]
points = [ ( l[::2], l[1::2] ) for l in points ]
for sub in points:
    plot([-x for x in sub[0]], [-y for y in sub[1]])
show()
