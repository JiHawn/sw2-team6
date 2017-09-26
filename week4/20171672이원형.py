import time

def factorial(n) :
      if n == 0 :
            return 1
      else :
            return n * factorial(n - 1)

def combination(n, r) :
      return factorial(n) / (factorial(r) * factorial(n-r))

def combination2(n,r) :
      if r == 0 :
            return 1
      elif n < r :
            return 0
      else :
            return combination(n-1, r-1) + combination(n-1, r)
while True:
	n = int(input("please int n first : "))
	if n == -1:
		break
	r = int(input("please int r : " ))
	if n <= 0 and r < 0:
		continue
	start = time.time()
	print(int(combination(n,r)))
	print("combination time : ",  "{:.10f}".format(time.time()-start))
	print(int(combination2(n,r)))
	start = time.time()
	print("combination2 time : ", "{:.10f}".format(time.time()-start))
