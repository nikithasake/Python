#prime numbers
'''It is a natural greater than 1 that has no positive divisors other than 1 and itself'''
n=int(input("Enter number:"))
if n>1:
	for i in range(2,n):
		if(n%i)==0:
			print(n,"it is not prime number")
			break
	else:
		print(n,"it is prime number")
else:
	print(n,"it is not prime number")

'''		
o/p:
Enter number:5
5 it is prime number

Enter number:1
1 it is not prime number

'''
