arr1=[ ['#','#','#','$','%','$'],['%','%','%','#','$','%'],['#','$','$','#','$','%']]
mat=list()
c1,c2,c3=0,0,0
for i in range(len(arr1)):
    matsub=list()
    c1=0
    c2=0
    c3=0
    for ele in arr1[i]:
        if ele=='$':
            c1+=1
        elif ele=='#':
            c2+=1
        else:
            c3+=1
    mat.append([c1,c2,c3])
o=0
maxlst=list()
maxval=0
     #0 1 2   0 1 2   0 1 2
# # # for ele in mat:# 2 3 0  #0 2 3  #3 0 2
# #                    # 0       1      2

for i in range(len(mat)):#0 1 2
    maxval=0
    for j in range(len(mat[0])):#0 1 2
        if maxval<mat[i][j]:
            maxval=mat[i][j]
    maxlst.append(maxval)# c1 c2 c3

for ele in maxlst:
    o+=len(arr1[0])-ele

print(o)