#0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8
x=int(input())
a=0
b=0
for i in range(1,x+1):
	if i%2!=0:
		a=a+2
	else:
		b=b+1
if(x%2!=0):
	print(a-2)
else:
	print(b-1)
