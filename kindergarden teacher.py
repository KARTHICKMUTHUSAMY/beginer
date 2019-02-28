def main():
	x=1
	y=int(input())
	for i in range(1,y):
		x=x*i
	print(x)
try:
	main()
except:
	print('invalid')
