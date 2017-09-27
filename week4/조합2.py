#팩토리얼을 이용하지 않고 구하기
def fact(n, m):
    sum = 1
    while n >= m:
        sum *=n
        n -=1
        return n
    return sum

def fac(j):
    um = 1
    for k in range(j +1):
        k +=1
        um *=k
    return um
a = int(input("nCr 의 n을 입력하시오."))
b = int(input("nCr 의 r을 입력하시오."))
c  = print (fact(a, b))
print (c/fac(b))