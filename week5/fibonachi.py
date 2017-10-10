import time
import random

def fibo(n) :
	if n <= 1:
		return n
	else:
		return fibo(n - 1) + fibo(n - 2)
def iterfibo(nbr) :
	iterfibo_list = []
	for i in range(0,nbr+1) :
		if i ==0 or i == 1 :
			iterfibo_list.append(i)
			idx = i
		else :
			iterfibo_list.append(int(iterfibo_list[i-2]+iterfibo_list[i-1]))
			idx = i
	return iterfibo_list[idx]
	
while True :
	nbr = int(input("Enter a number: "))
	if nbr == -1 :
		break
	ts = time.time()
	fibonumber =fibo(nbr)
	ts = time.time() -ts
	print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
	ts2 = time.time()
	fibonumber = iterfibo(nbr)
	ts2 = time.time() - ts2
	print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts2))
