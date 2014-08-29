#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
http://www.pythonchallenge.com/pc/def/peak.html
'''
# Since 2012

import pickle
import urllib.request

fd = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
data = pickle.load(fd)
fd.close()

print(data)
for l in data:
    print(''.join(t[1] * t[0] for t in l))
