
#팩토리얼을 이용하지 않고 구하기
def combi(n,r) :
      if r == 0 :
            return 1
      elif n < r :
            return 0
      else :
            return combi(n-1, r-1) + combi(n-1, r)
while True:
	n = int(input("첫번째 수를 입력 또는 -1을 입력하면 종료: "))
	if n == -1:
		break
	r = int(input("두번째 수를 입력:" ))
	if n <= 0 and r < 0:
		continue
	print(int(combi(n,r)))
 
