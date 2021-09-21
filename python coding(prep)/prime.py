#prime number or not
n=int(input("Enter number:"))
c=0
for i in range(1,n+1):
	if(n%i==0):
		c=c+1
		print(c)
if(c==2):
	print(n,"is prime number:")



