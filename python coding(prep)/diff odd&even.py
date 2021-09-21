#Given a maximum of 100 digit numbers as input, find the difference between the sum of odd and even position digits
n=[int(x) for x in str(input())]
print(type(n))
even=0
odd=0
for i in range(len(n)):
	if i%2==0:
		even=even+n[i]
	else:
		odd=odd+n[i]
print(even-odd)
