M,T2,T3,T4=list(map(int,input().split()))
a=[]
if ((M in range(1,100000)) and (T2 in range(0,50000)) and (T3 in range(0,50000)) and (T4 in range(0,50000)) ):
    for i in range(M):
        ing,*ingname=input().split()
        ing=int(ing)
        ingname=list(map(str,ingname))
        dic={ing:ingname}
        a.append(dic)
for i in range(M):
    print(a[i])
