import math
def main():
	x=int(input())
	while(y!=0):
		l=math.sqrt(x)
		if l==int(l):
			print(int(l))
			break
		else:
			x=x-1
	if x==0:
		print('no')
    
try:
  main()
except:
  print('invalid')
  
