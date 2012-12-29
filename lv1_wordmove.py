#! C:\Python27\python.exe
import sys

#list1 = list('g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.')

list1 = list('http:////www.pythonchallenge.com//pc//def//map.html')

for c in list1:
    t = c
    if c >= 'a' and c <= 'z':
        t = chr(ord(c)+2)
    if c == 'y':
        t = 'a'
    if c == 'z':
        t = 'b'
    sys.stdout.write(t)
