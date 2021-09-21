#perfect number
'''perfect number is a positive integer that is equal to the sum of its positive divisors excluding the number itself'''

'''Eg:no=4..1,2 so 1+2=3..it is not perfect'''
'''EG:no=6..1,2,3 so 1+2+3=6..so 6==6 it is perfect number'''

'''perfect number is a positive integer that is equal to the half of the sum of its all positive divisors'''

'''Eg:no=4..1,2,4 so 1+2+4=7 so 7/2 =3.5 so 4=!=3.5..it is not perfect'''
'''EG:no=6...1,2,3,6 so 1+2+3+6=12 so 12/2 so 6==6 it is perfect number'''

n=int(input("Enter number:"))
res=0
for i in range(1,n):
	if (n%i)==0:
		res=res+i
if res==n:
	print(n,"it is perfect number")
else:
	print(n,"it is not perfect number")

'''
o/p:
Enter number:6
6 it is perfect number
'''

