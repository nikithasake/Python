#GCD/HCF of two numbers
'''Eg:
12                    14
1,2,3,4,6,12           1,2,7,14
==>Common are 1,2 in this 2 is highest so 2 is GCD Oof 12 & 14'''
#Eculid algorithm is used to findout the GCD of the two numbers
'''Eg:
(a)      (b)
64       48
(a) (b)     (a%b)
64 =48*x+remainder
64=48*1+16
(b) (a%b)
48= 16*3+0
(a%b)
16 = 0
so 16 is the GCD of 64 and 48'''
'''Eg:
4 18
take bigger value at LHS and smaller value at RHS
18=4*x+remainder
18=4*4+2
4=2*2+0
2=0
2 is the GCD of 4 and 18'''

'''
import math
print(math.gcd(4,18))

''' 

'''
o/p:
2
'''

def GCD(a,b):
	if b==0:
		return a
	else:
		return GCD(b,a%b)
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
print(GCD(n1,n2))

'''
o/p:
Enter the first number:4
Enter the second number:18
2
'''






















