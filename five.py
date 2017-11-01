def even_or_odd():

	number = int(input("Enter number:"))

	if number % 2 == 1:
		print("{} is odd".format(number))
	elif number % 2 == 0:
		print("{} is even".format(number))

even_or_odd()

# "Dear Mr.{} {}".format("John","Murphy")