def combination(n,r) :
      if r == 0 :
            return 1
      elif n < r :
            return 0
      else :
            return combination(n-1, r-1) + combination(n-1, r)
n = int(input("please input n first : "))
r = int(input("please input r : " ))
print(combination(n,r))
