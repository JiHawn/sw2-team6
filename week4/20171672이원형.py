def factorial(n) :
      if n == 0 :
            return 1
      else :
            return n * factorial(n - 1)

def combination(n, r) :
      return factorial(n) / (factorial(r) * factorial(n-r))

n = int(input("please int n first : "))
r = int(input("please int r : " ))
print(combination(n,r))
