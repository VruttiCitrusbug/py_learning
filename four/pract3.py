arr=[
    [1,2,3,4,5,100],
    [1,2,3000,4,5,55],
    [1,2,3,4,5,4],
    [6,6,6,6,6,9],
    [9,9,9,9,9,20],
    [222,222,222,222,222,222],
    [4,5,6,7,78,6]
]
c2=1

lst1=list()
lst2=list()
lst3=list()
maxsum=0
tot=0
for i in range(0,len(arr)-2):
    c2=1
    for x in range(len(arr[0])-2): 
        lst1.clear()
        lst2.clear()
        lst3.clear()
        # print()
        for j in range(x,x+3):
            lst1.append(arr[i][j])
        lst2.append(arr[i+1][c2])
        c2+=1
        for j in range(x,x+3):
            lst3.append(arr[i+2][j])
        tot+=1
        if maxsum<(sum(lst1)+sum(lst2)+sum(lst3)):
            maxsum=sum(lst1)+sum(lst2)+sum(lst3)
print("total i is".format(tot))
print("max sum is {}".format(maxsum))