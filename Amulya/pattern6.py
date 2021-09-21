#pattern
n=input("Enter string:")
l=len(n)
for i in range(l):
	for j in range(i+1):
		print(n[j],end=" ")
	print()

'''
o/p:
Enter string:nikitha
n 
n i 
n i k 
n i k i 
n i k i t 
n i k i t h 
n i k i t h a 
'''
