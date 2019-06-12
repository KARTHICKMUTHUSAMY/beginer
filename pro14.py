a,b=map(int,input().split())
x=list(map(int,input().split()))
c=0
for i in range(0,b):
  u,v=map(int,input().split())
  b=x[u-1:v]
  for j in b:
    c=c^j
  print(c)
  c=0
