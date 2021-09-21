#Selection sort Algorithm
def selection(list):
	l=len(list)
	for i in range(l):
		for j in range(i+1,l):
			if list[i]>=list[j]:
				list[i],list[j]=list[j],list[i]
	return list


list=eval(input("Enter list:"))
s=selection(list)
print(s)
