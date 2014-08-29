#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
http://www.pythonchallenge.com/pc/def/map.html
'''
# Since May 24 2012

# v1

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(''.join(chr(ord(c)-24) if c >= 'y' else 
        chr(ord(c)+2) if c >= 'a' and c <= 'z' else c
        for c in s))
