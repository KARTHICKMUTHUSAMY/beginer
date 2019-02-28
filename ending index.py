import fractions
p,q=input().split()
n=int(p)
q=int(q)
if(p>=1 and p<=100000):
    p=(list(map(int,input().split())))
    for i in range(0,q):
        j,k=input().split()
        j=int(j)
        k=int(k)
        x=j-1
        y=k-1
        sum=0
        print(min(p[x],p[y]))
