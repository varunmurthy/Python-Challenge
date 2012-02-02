f = open('./Challenge2.txt','r')
for line in f:
    for a in line:
        if a.isalpha():
            print "".join(a)
            
    