v1 = int(input())
k1 = list(map(int,input().split()))
c1,l = 0,[]
b1 = [x for x in range(1,v1+1)]
for i in k1:
  if i in b1:
    b1.remove(i)
k = 0
for i in range(0,v1-1):
  p = k1[i]
  for j in range(i+1,v1):
    if p == k1[j]:
      if p < b1[k]:
        k1[j] = b1[k]
        c1 += 1
      else:
        k1[i] = b1[k]
        c1 += 1
      k += 1
print(c1)
print(*k1)
