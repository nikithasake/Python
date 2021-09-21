#1,2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17…
n=int(input())
a=1
b=0
sum=1
for i in range(1,n+1):
	if i%2!=0:
		print(sum,end=" ")
		a=b
		b=sum
		sum=a+b
s=0
for i in range(2,n+1):
	if(n%i==0):
		print(n-1)
	
