str=input()

flag3=0

for i in range(0,len(str)-1):

  for j in range(i+1,len(str)):

    if str[i]<str[j]:

      flag3=1

      print(str[j:])

      break

  if flag3==1:

    break

else:

  print(str)
