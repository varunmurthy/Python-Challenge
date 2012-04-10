import pickle

val = pickle.load(open('banner.p','rb'))

for line in val:
    op = '' 
    for a,b in line:
        op = op+(a*b)
    print op
