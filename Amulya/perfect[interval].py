#perfect within interval
'''perfect number is a positive integer that is equal to the sum of its positive divisors excluding the number itself'''
l=int(input("Enter lower number:"))
u=int(input("Enter upper number:"))
for num in range(l,u+1):
	res=0
	for i in range(1,num):
		if (num%i)==0:
			res=res+i
	if num==res:
		print(num)
		
'''
o/p:
Enter lower number:1
Enter upper number:10
6

Enter lower number:1
Enter upper number:30
6
28

'''
