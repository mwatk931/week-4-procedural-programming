total = 0

for number in range(100):
	if number % 2 == 0 and number % 3 != 0:
		total += number

print(total)
