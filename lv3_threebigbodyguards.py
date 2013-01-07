#! C:\Python27\python.exe

import re

f = open('lv3_source','r')

linestring = f.read()

f.closed

#print linestring

pattern = re.compile(r'piq')

for line in linestring:
    match = pattern.match(line)
    if match:
        print 'match'
        print match.group()
