import csv
d=dict()
i=0
j=0
e=dict()
try:
    with open(r'csvv1.csv','r') as csvfile:
        r=csv.DictReader(csvfile)
        for ele in r: 
            d[i]=ele
            i+=1
except:
    print("cannot open")
i=0
m=None
x=list()
for ele in d.values():
    for e in ele.keys():
        if ele[e]=='':
            x.append(e)
            m=i
    i+=1
for q in x:
    del d[m][q]  
for x in range(len(d)):
    if d[x]=={}:
        del d[x]
for ele in d.values():
        print(ele)