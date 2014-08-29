#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
Since May 29 2012
Look-and-say sequence
http://www.pythonchallenge.com/pc/return/bull.html
Examples:
>>> s = '1'
>>> for i in range(30):
...     s = looksay_my(s)
>>> len(s)
5808

>>> s = '1'
>>> seq = looksay_lc(s)
>>> for i in range(30):
...     _crap = seq.next()
...     if i == 29:
...         len(seq.next())
5808

>>> s = '1'
>>> for i in range(30): s = looksay_groupby(s)
>>> len(s)
5808
>>>
'''

from collections import defaultdict
from itertools import groupby

# v1

def looksay_my(s):
    prev, l, group, d = s[0], [], 0, defaultdict(int)
    d[prev] += 1
    l.append(d)

    for c in s[1:]:
        if c == prev:
            l[group][c] += 1
            continue
        d = defaultdict(int)
        d[c] += 1
        l.append(d)
        group += 1
        prev = c
    return ''.join(''.join((str(v),k)) for d in l for k,v in d.items())
        
# v2 

# More from http://en.wikipedia.org/wiki/Look-and-say_sequence

def looksay_lc(s): # List Comprehension
    while True:
        yield s
        # print s,
        bp = [0] + [ i for i in range(1, len(s)) if s[i-1] != s[i] ] \
                 + [len(s)] # breakpoints
        gp = [ s[bp[i-1] : bp[i]] for i in range(1, len(bp)) ] # groups
        s = ''.join( str(len(g)) + g[0] for g in gp )
        # print bp, gp, s

# v3

# More from http://stackoverflow.com/questions/6972764
def looksay_groupby(s):
    return ''.join( str(len(list(g))) + k for k, g in groupby(s) )

if __name__ == '__main__':
    import doctest
    doctest.testmod()
