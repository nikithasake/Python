val = int(input('enter the number: '))
x=0
y=0
for i in range(1,val+1):
	print(i)
	if(i%2!=0):
		x=x+7
		print(x)
	else:
		y=y+6

if(val%2!=0):
	print(' {} term in accordance to the program is {}'.format(val,x-7))

else:
	print('{} term in accordance to the program is {}'.format(val,y-6))
	
	
#o/p:
0,0,7,6,14,12,21,18, 28
