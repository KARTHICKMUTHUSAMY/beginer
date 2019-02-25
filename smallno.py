x=input()
y=input()
z=list(str(x))
r=y
while r>0:
    r=r-1
    del(z[r])
print(''.join(z))
