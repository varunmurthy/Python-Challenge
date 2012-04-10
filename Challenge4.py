import urllib2
import re
nothing  = '56060'
# at 16044 they want to divide by 2

for i in range(400):
    filehandle = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+nothing)
    temp = filehandle.read()
    m = re.search('and the next nothing is (\d.*)',temp)
    print temp,m.group(1)
    nothing = m.group(1)
