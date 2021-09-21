#leap year or not
year=int(input("Enter year:"))
if (year%400==0):
	print(year,"It is a leap year")
elif(year%4==0 and year%100!=0):
	print(year,"it is a leap year")
else:
	print("not a leap year")
