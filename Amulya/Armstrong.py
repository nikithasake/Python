#Armstrong Numbers
'''Eg:
22==>here 2 digits are present so n=2==>2^2=4;2^2=4 so 4+4=8==>8!=22==>it is not armstrong
Eg:
153==>here 3 digits are present so n=3==>1^3+5^3+3^3 so 1+125+27=153==>153==153==>it is armstrong'''
n=int(input("Enter value:"))
i=n
r=0
l=len(str(n))
while n>0:
	a=n%10
	n=n//10
	r=r+a**l
print(r)
if(r==i):
	print(r,"it is armstrong number")
else:
	print(r,"it is not armstrong number")
	
	
