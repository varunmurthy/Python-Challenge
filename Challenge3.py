import re
f = open('./Challenge3.txt','r')
list = []

for x in  f:
    m = (re.search('[^A-Z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][^A-Z]',x))
    if m:
        list.append((m.group(0)[4]))

print ''.join(list)

     