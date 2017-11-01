a_list = [8, 2, 3, -1, 7]

def addNumbers():

	total = 0

	for number in a_list:
		total = total + number

	print(total)



def multNumbers():

	total = 1

	for number in a_list:
		total = total * number

	print(total)



def main():

	sum_of_list = addNumbers()
	mult_of_list = multNumbers()

main()