def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)
while True:
	a = input("input number : ")
	if a == -1:
		break
	elif int(a) != float(a):
		print ("please int integer")
		a = int(input("input number again :"))

	else:
		print(factorial(a))
	
	
