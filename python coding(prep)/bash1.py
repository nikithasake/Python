n=int(input("Enter input:"))
arr=[]
for i in range(1,n+1):
	ele=int(input())
	arr.append(ele)
print(arr)
a=sorted(arr)
print(a)
for i in a:
	if(a[i]==i+1):
		continue
	else:
		print("Missing number is",i+1)
		break
'''
o/p:
Enter input:5
1
2
3
6
4
[1, 2, 3, 6, 4]
[1, 2, 3, 4, 6]
Missing number is 5
'''
