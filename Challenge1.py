#
#a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#a = "map"
#for x in a:
#    if x != ' ':
#        y=ord(x)+2
#        print chr(y).rstrip()
#    else:
#        print ' '

a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print "".join([chr(ord(x)+2) for x in a])

# Lessons Learned
# Make Trans maps a dictionary of elements to another. Both the from and to strings can be mentioned in a single string format.
