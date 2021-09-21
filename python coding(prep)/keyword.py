import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
input_var = input("Enter word:").capitalize()
if input_var in keyword.kwlist:
    print(input_var+ " is a keyword")
else:
    print(input_var+ " is a not keyword")

