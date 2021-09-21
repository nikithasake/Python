#pattern
'''
*
* *
*  *
*   *
** ***
'''

n=int(input("Enter the number of rows:"))
for i in range(n):
	for j in range(n):
		if j==0 or i==(n-1) or i==j:
			print("*",end="")
		else:
			print(end=" ")
	print()
