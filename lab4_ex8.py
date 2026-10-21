pos = int(input("Enter a positive integer: "))

factorial = 1
for i in range(1, pos + 1):
    factorial *= i

print(factorial)