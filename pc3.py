#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
http://www.pythonchallenge.com/pc/def/equality.html
'''
# Since May 24 2012

import re

pat = r'[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+'
          #            ^     ^
          # Note the parentheses
with file('pc3-chars') as fd:
    print ''.join(re.findall(pat, fd.read()))
