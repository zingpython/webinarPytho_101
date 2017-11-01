word = input("Please enter a string:")

letter = 0
digit = 0
space = 0

for i in word:
	if i.isalpha():
		letter = letter + 1
	elif i.isdigit():
		digit = digit + 1
	else:
		space = space + 1 

print("Letters", letter)
print("Numbers", digit)
print("Spaces", space)