val1,val2=map(int,input().split())
val3,val4=map(int,input().split())
val5,val6=map(int,input().split())
val7,val8=map(int,input().split())
t1=val4-val2
t2=val6-val8
t3=val5-val3
t4=val7-val1
if t1==t2==t3==t4:
  print("yes")
else:
  print("no")
