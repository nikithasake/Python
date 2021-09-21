#factorial without recursion
n=int(input("Enter the number:"))
res=1
for i in range(n,0,-1):
	res=res*i
print(res)
