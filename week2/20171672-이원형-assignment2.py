def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)
while True:
	a = int(input("input number : "))
	if a == -1:
		break
	else:
		print(factorial(a))
	
	
