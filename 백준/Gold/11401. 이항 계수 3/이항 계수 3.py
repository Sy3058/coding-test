n, k = map(int, input().split())
p = 1000000007
# nCk = n! / k!(n-k)!

def fact(n):
  a = 1
  for i in range (2, n+1):
    a = (a * i) % p
  return a

# 거듭제곱 계산
def square(n, k):
  if k == 0:
    return 1
  elif k == 1:
    return n
  
  tmp = square(n, k//2)
  if k % 2 == 1:
    return tmp * tmp * n % p
  else:
    return tmp * tmp % p
  
top = fact(n)
bottom = fact(k) * fact(n-k) % p

# 페르마의 소정리를 이용
print(top * square(bottom, p-2) % p)