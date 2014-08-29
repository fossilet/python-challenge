#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
http://www.pythonchallenge.com/pc/def/ocr.html
'''
# Since May 24 2012

# v1

with file('pc2-chars') as fd:
    rare = ( c for c in fd.read() if c>='a' and c<='z' )
#                      ^^^^^^^^^ bad
print ''.join(rare)

# v2 

with file('pc2-chars') as fd:
    rare = ( c for line in fd for c in line if c>='a' and c<='z' )
    print ''.join(rare)
#   ^^^^^ the file must be open when printing

# v3

print''.join(c for l in file('pc2-chars')for c in l if c>='a'and c<='z')

# v4

print ''.join(c
        for l in file('pc2-chars')
            for c in l 
                if c>='a' and c<='z')
