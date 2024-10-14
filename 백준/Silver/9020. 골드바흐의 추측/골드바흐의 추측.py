n = int(input()) # number of test case

def prime(n):
  if n == 1:
    return False
  for i in range (2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

for _ in range (n):
  num = int(input())

  l = num // 2 # 두 수 중 줄어드는 변수
  r = num // 2 # 두 수 중 늘어나는 변수

  for _ in range (num//2):
    if prime(l) and prime(r): # 두 수 모두 소수라면
      print(l, r)
      break
    else:
      l -= 1
      r += 1