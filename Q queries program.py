def hcf(x,y):
	while(y!=0):
		z=y
		b=x%y
		x=z
	return x
def main():
	n=int(input())
	q=int(input())
	(l,r)=([],[])
	for i in range(n):
		l.append(int(input()))
	print(l)
	for c in range(q):
		x=int(input())
		y=int(input())
		r.append(hcf(l[x-1],l[x-1]))
	for i in r:
		print(r)
try:
  main()
except:
  print('invalid')
  p
