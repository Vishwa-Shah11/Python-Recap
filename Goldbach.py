from math import sqrt

def isPrime(n):
  flag = 0
  if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            flag = 1
            break
    if (flag == 0):
        return True
    else:
        return False
  else:
      return False

def Goldbach(n):
    #primelist = []
    #for i in range(1,n+1):
    #  if (isPrime(i)):
    #    primelist.append(i)
    #print(primelist)
    l1 = []
    for i in range(3,(n//2)+1):
        if isPrime(i) and isPrime(n-i):
            print(i,n-i)
            l1.append((i,n-i))
    return l1


    
n=int(input())
print(sorted(Goldbach(n)))