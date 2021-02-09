M,T2,T3,T4=list(map(int,input().split()))
x=0
y=0
z=0
for i in range(1,T2+1):
    for j in range(1,T3+1):
        for k in range(1,T4+1):
            if (2*i)+(3*j)+(4*k)==M and (T2-i)<=(T3-j)<=(T4-k):
                x=i
                y=j
                z=k
print(x,y,z)
