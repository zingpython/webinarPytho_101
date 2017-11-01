a_list = [1,3,55,1,9,4,56,2,1,8]

counter = 0
print("At start counter is", counter)

for number in a_list:
	if number == 1:
		counter = counter + 1
		print("Now counter is", counter)

print("Total", counter)