k=list(input())
v=list(input())
m=len(x)
d=0
i=0
while m>0:
    d=d+(ord(v[i])-ord(k[i]))
    i=i+1
    m=m-1
print(d)
