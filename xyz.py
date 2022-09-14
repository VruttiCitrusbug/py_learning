import csv
d=dict()
i=0
lines = [['vrutti','patel','21','1234','28'],
['saloni','modi','21','4321','12'],
['parth','machi','22','42356','4'],
['nikhil','vyas','21','12123123','23'],
['henil','dave','30','12312','22'],
['madhav','trivedi','22','1231','22'],
['gaurang','prajapati','22','121212','11'],
['dhruvi','paterl','21','12311231','22'],
['darshan','parikh','22','1323','3'],
['akshay','nair','21','1231233','4'],
['saumya','munshi','22','112233','7'],
['pragya','gupta','22','12312313','8'],
['vansh','rathod','22','122313','15'],
['parmeet','lalvani','21','312213','23'],
['sneha','shukla','23','313313','21'],
['khushi','bagadiya','22','121123','22'],
['jeet','rachela','25','12133','17'],
['karan','bahtiya','22','12313','3'],
['mayank','makvana','22','13133','23'],
['raj','barot','24','13123','2'],
['dhruvil','dave','21','12333','23'],
['kunj','thakkar','27','13123','21'],
['kaushal','prajapati','22','123123','30'],
['manthan','derasari','22','1231234124','5'],
]
header = ['nam','surname','age','number','dob']

with open("xyz.csv", "w") as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header) # write the header
    # write the actual content line by line
    for l in lines:
        writer.writerow(l)
try:
    with open('C:\Users\Vrutti\Downloads\csvv1.csv','r') as csvfile:
        r=csv.DictReader(csvfile)
        for ele in r: 
            d[i]=ele
            i+=1
        for ele in d.values():
            print(ele)
except:
    print("cannot open")