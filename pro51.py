num1=int(input())
li=list(map(int,input().split()))
n2=[]
n3=1
for i in range(num1):
  v=li[i:]
  ans=len(v)
  for j in range(ans-1):
    if v[j]>0 and v[j+1]<0:
      n3=n3+1
    elif v[j]<0 and v[j+1]>0:
      n3=n3+1
    else:
      break
  n2.append(str(n3))
  n3=1
print(" ".join(n2))
