#fibonacci
n=int(input("Enter how many u want in this series:"))
first=0
second=1
for i in range(n):
	print(first)
	temp=first
	first=second
	second=temp+first
	
