#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
http://www.pythonchallenge.com/pc/return/evil.html
http://www.pythonchallenge.com/pc/return/evil1.jpg
http://www.pythonchallenge.com/pc/return/evil2.jpg
http://www.pythonchallenge.com/pc/return/evil2.gfx
http://www.pythonchallenge.com/pc/return/evil3.jpg
http://www.pythonchallenge.com/pc/return/evil4.jpg
'''
# Since May 30 2012


with open('evil2.gfx') as fd:
    data = fd.read()

# v1

for i in range(5):
    with open('evil-%d' % i, 'w') as fd:
        fd.write(data[i::5])

# v2

# This is slower than v1, probably for traversing the list byte by byte

'''
fds = [ open('evil-%d' % i, 'w') for i in range(5) ]

for i in range(len(data)):
    num = i % 5
    fds[num].write(data[i])

for fd in fds:
    fd.close()
'''
