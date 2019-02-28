def stair():
	x=0
	y=[]
	z=int(input())
	for i in range(z):
		y.append(int(input()))
	for i in y:
		x+=(z-i)
	print(x)
  
try:
  stair()
except:
  print('invalid')
  p
