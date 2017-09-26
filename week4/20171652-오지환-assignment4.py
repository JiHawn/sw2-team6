def facto(num):
	return 1 if num == 0 else facto(num - 1) * num

while True:
	num = int(input("Enter a number: "))
	if num == -1:
		break
	print("%d! = %d" %(num, facto(num)))
