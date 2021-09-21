#Lcm of a number
def lcm(n1,n2):
	if n1>n2:
		high=n1
	else:
		high=n2
	value=high
	while True:
		if high%n1==0 and high%n2==0:
			print(high)
			break
		else:
			high=high+value
n1=int(input("Enter n1 value:"))
n2=int(input("Enter n2 value:"))
lcm(n1,n2)
