def reverse(string):
	reverse_string=" "
	for i in string:
		reverse_string=i+reverse_string
	print("reversed string:",reverse_string)
string=input("Enter string:")
reverse(string)

'''
o/p:
Enter string:nikki
reversed string: ikkin 
'''
