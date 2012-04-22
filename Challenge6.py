#!/usr/local/bin/python
import zipfile
import re
from warnings import catch_warnings
# Open zip file
z = zipfile.ZipFile('channel.zip', 'r')

## ZipFile.read returns the bytes contained in named file
names = z.namelist()

#comments = z.comment
zinfo = z.infolist()
commentlist = []

#Start from random file number
name = '90052.txt' 
for i in range(len(names)):
    f = z.open(name)
    temp = f.read()
#    print i, name, temp, "Comments"
    try:
        m = re.search('nothing is (\d*)', temp)
        name = m.group(1)+'.txt'
    except Exception:
        break

    commentlist.append(z.getinfo(name).comment)

print "".join(commentlist)
    
    