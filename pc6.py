#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
http://www.pythonchallenge.com/pc/def/channel.html
'''
# Since May 25 2012

from zipfile import ZipFile

zfd = ZipFile('channel.zip')
text = zfd.read('90052.txt')
fname = '{}.txt'.format(text.split()[-1])
comment = []

while True:
    try:
        text = zfd.read(fname)
        fname = '{}.txt'.format(text.split()[-1])
        comment.append(zfd.getinfo(fname).comment)
        print fname
    except:
        break

print ''.join(comment)
