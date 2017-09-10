#팩토리얼 구하는 함수 
def fac(a): 
    if a == 0:
        return 1
    return a * fac(a - 1) 

# 반복적으로 돌려줌 
while True:
    n = str(input())
    '''if float(n) == n:
        print ("정수를 입력하시오")
        float(n) == int(n)'''
    if int(n) == -1: #-1일 경우 함수를 빠져나옴 
        break
    elif int(n) < 0: #예외처리
        print("양의 정수를 입력하시오")

    else:
        print(fac(int(n))) 
