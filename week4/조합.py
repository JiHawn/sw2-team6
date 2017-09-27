def fact(n) :
      if n == 0 :
            return 1
      else :
            return n * fact(n - 1)

def combi(n, r) :
      return fact(n) / (fact(r) * fact(n-r))

n =int(input("input first number:"))
r = int(input("input second number:"))
while n <r:
    print("다시입력해주세요")
    n =int(input("input first number:"))
    r = int(input("input second number:"))
print (combi(n, r))
