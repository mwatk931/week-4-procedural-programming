count = 0

for number in range(2000, 3000):
	if number % 13 == 0:
		count += 1
		if count == 2:
			print(number)
			break
