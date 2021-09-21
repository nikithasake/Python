#pattern
n=int(input("Enter rows:"))
for i in range(n,0,-1):
	for j in range(1,i+1):
		print(j,end=" ")
	print()

'''	
o/p:
Enter rows:5
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''
