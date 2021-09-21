#series:4,9,7,12,10,15,13
a=int(input())
N=int(input())
term=0
for i in range(1,N):
	if i%2!=0:
		term=a+5
	else:
		term=term-2
		a=term
print(term)

'''o.p:a=4
	 n=5
	 10''
