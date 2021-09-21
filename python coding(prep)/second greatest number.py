#Second Greatest of three numbers
n=int(input())
l=[]
for i in range(n):
	x=int(input("Enter value:"))
	l.append(x)
l.sort()
print(l[-2])
	
