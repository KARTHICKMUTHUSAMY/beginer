num=input()

flag=0

for i in range(1,len(num)):

  j=0

  while j<len(num) and len(num[:j]+num[i+j:])==len(num)-i:

    n=num[:j]+num[j+i:]

    if int(n)%8==0:

      flag=1

      print('yes')

      break

    j+=1

  if flag==1:

      break

else:

  print('no')
