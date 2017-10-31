import time

def fibo(n) : #recursive
	if n <= 1:
		return n
	else:
		return fibo(n - 1) + fibo(n - 2)

def iterfibo(nbr) : #loop using list
	iterfibo_list = []
	for i in range(0,nbr+1) :
		if i ==0 or i == 1 :
			iterfibo_list.append(i)
			idx = i
		else :
			iterfibo_list.append(int(iterfibo_list[i-2]+iterfibo_list[i-1]))
			idx = i
	return iterfibo_list[idx]

def iterfibo2(nbr) : #loop using variable
	a, b = 0,1 
	if nbr == 0 :
		return a
	else :
		count = 2
		while count <= nbr :
			a,b= b,a+b
			count +=1
		return b

def iterfibo3(n):
        if n == 0:
                return 0
        elif n == 1:
                return 1
        a = [1]
        for i in range(n):
                try:
                        a[2] = a[0] + a[1]
                        a[0] = a[1]
                        a[1] = a[2]
                except:
                        a.append(1)
        return a[2]
	
while True :
	try:
		nbr = int(input("Enter a number: "))
	except:
		continue
	if nbr == -1 :
		break
	ts = time.time()
	fibonumber =fibo(nbr)
	ts = time.time() -ts
	print("Fibo_rec(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

	ts2 = time.time()
	fibonumber = iterfibo(nbr)
	ts2 = time.time() - ts2
	print("Fibo_loop_using_list(%d)=%d, time %.6f" %(nbr, fibonumber, ts2))

	ts3 = time.time()
	fibonumber2 = iterfibo2(nbr)
	ts3 = time.time() - ts3
	print("Fibo_loop_using_variable(%d)=%d, time %.6f" %(nbr, fibonumber2, ts3))

	ts4 = time.time()
	fibonumber3 = iterfibo3(nbr)
	ts4 = time.time() - ts4
	print("Fibo_loop_using_list2(%d)=%d, time %.6f" %(nbr, fibonumber3, ts4))
