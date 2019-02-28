x=list(input())
y=list(input())
z=len(x)
s=len(y)
i=0
j=0
c=[]
while z>0:
    if x[i]==y[j]:
        c.append(x[i])
    j=j+1
    i=i+1
    z=z-1
print(s-len(c))
