#Reverse of a number
n=int(input("Enter number:"))
r=0
while n>0:
	a=n%10
	print(a)
	n=n//10
	print(n)
	r=r*10+a
print("it is reverse:",r)
