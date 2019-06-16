n=int(input())
a=2
t=3
p=3
while a<n+1:
    if t==1:
        t=2*p
        p=t
    else:
        t=t-1
    a=a+1
print(t)
