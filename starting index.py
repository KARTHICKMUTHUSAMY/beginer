def sum(l,s,e):
	x=0
	for i in range(s,e+1):
		x+=l[i]
	print(x)

def main():
	n=int(input('N:'))
	l=[]
	for i in range(1,n):
		l.append(int(input('Enter array :')))
	q=int(input('Q:'))
	for i in range(q):
		u=int(input())
		v=int(input())
		sum(l,u,v)
try:
	main()
except:
	print('invalid')
