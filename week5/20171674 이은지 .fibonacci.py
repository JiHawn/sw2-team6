import time
import random
#재귀함수을 이용하여 작성
def fibo(n):
	if n <= 1:
		return n
	return fibo(n - 1) + fibo(n - 2)
#반복적으로 구현
#피보나치는 0과 1로 시작하며 다음 피보나치수는 앞의 두수의 합
def iterfibo(m):
        a, b =0, 1
        if m == 0 :
                return a
        else:
                count = 2
                while count <= m:
                        a, b = b, a+b
                        count +=1
                return b

while True:
	nbr = int(input("Enter a number: "))
	if nbr == -1:
		break
	ts = time.time()
	fibonumber = iterfibo(nbr)
	ts = time.time() - ts
	print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
	ts =time.time()
	fibonumber = fibo(nbr)
	ts = time.time() - ts
	print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
