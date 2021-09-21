#finonacci series
n=int(input())
a=0
b=1
sum=0
if n<=0:
	print("ENter valid numebr:")
else:
	for i in range(n):
		print(sum,end=" ")
		a=b
		b=sum
		sum=a+b
	
