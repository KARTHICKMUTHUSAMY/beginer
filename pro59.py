a,y=map(str,input().split("|"))
c=input()
if len(a)>len(y):
  if len(a)==len(y+c):
    print(a+"|"+y+c)
elif len(a)<len(y):
  if len(a+c)==len(y):
    print(a+c+"|"+y)
elif len(a)==len(y) and len(c)>1 or (len(y)or len(a))==0:
  print("Impossible")
