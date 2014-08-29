#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
http://www.pythonchallenge.com/pc/return/cat.html
http://www.pythonchallenge.com/pc/return/uzi.html
'''
# Since May 31 2012

# TODO: not finished
from datetime import datetime

for y in range(1800, 2013):
    if datetime(y, 1, 26).weekday() == 0:
        print(y)
