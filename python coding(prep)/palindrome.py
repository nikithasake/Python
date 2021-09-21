#Palindrome or not
n=int(input("Enter number:"))
i=n
print(i)
r=0
while n>0:
	a=n%10
	n=n//10
	r=r*10+a
if(i==r):
	print(i,"is a palindrome")
else:
	print(i,"it is not palindrome")
	
