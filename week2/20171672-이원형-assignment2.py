def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)
a = input("input number")
while True:
	if a == -1:
		break
	elif int(float((a))) != float(a):
		print ("please int integer")
		a = input("input number again :")

	else:
		print(factorial(int(float(a))))
		a = input("input number")
	
	
