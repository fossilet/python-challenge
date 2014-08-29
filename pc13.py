#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
http://www.pythonchallenge.com/pc/return/disproportional.html
'''
# Since May 30 2012

# From http://holger.thoelking.name/python-challenge/13

from xmlrpclib import ServerProxy
conn = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print conn.phone("Bert")
