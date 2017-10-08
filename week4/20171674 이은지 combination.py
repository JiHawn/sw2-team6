# 팀별 수업 이후 
#효율성 검사를 시간을 재서 factorial을 이용한 코드와 안이용한 코드 시간비교 
import time 
#factorial 이용
def fact(n):
      if n == 0:
            return 1
      else:
            return n * fact(n - 1)

def combi(n, r):
      return fact(n) / (fact(r) * fact(n-r))
# factorial 이용안함
def combi2(n,r):
      if r == 0:
            return 1
      elif n < r:
            return 0
      else:
            return combi(n-1, r-1) + combi(n-1, r)
while True:
	n = int(input("첫번째 수를 입력 또는 -1을 입력하면 종료:"))
	if n == -1:
		break
	r = int(input("두번째 수 입력: " ))
	if n <= 0 and r < 0:
		continue
	start = time.time()
	print(int(combi(n,r)))
	print("combi time : ",  "{:.10f}".format(time.time()-start))
	print(int(combi2(n,r)))
	start = time.time()
	print("combi2 time : ", "{:.10f}".format(time.time()-start))
