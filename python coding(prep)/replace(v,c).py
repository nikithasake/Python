#
vowel=['a','e','i','o','u']
a=str(input())
b=str(input())
c=str(input())
for x in a:
	if x in vowel:
		a=a.replace(x,"*")
print(a)
for y in b:
	if y not in vowel:
		b=b.replace(y,"@")
c=c.upper()
print(a+b+c)

'''#o/p:
Input
    how
    are
    you
Expected Output : h*wa@eYOU'''
