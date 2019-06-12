num=int(input())

i=0

x=0

b=[]

while i<90 and i<num:

  r=0

  for j in str(num-i):

    r+=int(j)

  if r+(num-i)==num:

    x+=1

    b.append(num-i)

  i+=1

print(x)

for i in b:

  print(i)
