x=list(input())
y=list(input())
z=len(x)
d=0
i=0
while z>0:
    d=d+(ord(y[i])-ord(x[i]))
    i=i+1
    z=z-1
print(d)
