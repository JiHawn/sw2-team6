def factorial(n):
	if n == 0 :
		return 1
	else:
		return n * factorial(n - 1)
a = input("input number : ")
while True:
	if int(a) == -1:
		break
	elif int(float((a))) != float(a):
		print ("please input integer")
		a = input("input number again :")
	elif int(a)<0 and int(a) != -1 :
		print("please input positive number")
		a= input("Input number again :")
	else:
		print(factorial(int(float(a))))
		a = input("input number : ")
	
	
