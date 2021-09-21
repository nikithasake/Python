'''a=0
b=0
n=int(input("Enter a number:"))
print(n)
for i in range(1,n+1):
	if(i%2!=0):
		if(i>1):
			a=a+2
	else:
		b=a/2
if(n%2!=0):
	print("a value:",a)
else:
	print("b value:",int(b))'''
	
n=int(input())
if n%2!=0:
	print(n-1)
else:
	print((n/2)-1)
