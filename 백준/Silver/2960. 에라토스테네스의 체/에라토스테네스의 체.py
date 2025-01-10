import sys

n, k = map(int, sys.stdin.readline().split())

num = [True for _ in range (n+1)]

def sieve():
  cnt = 0
  for i in range (2, n+1):
    if num[i] == True: # i가 소수인 경우
      cnt += 1
      if cnt == k:
        return i
      j = 2
      while i * j <= n:
        if num[i*j] == True:
          num[i*j] = False
          cnt += 1
          if cnt == k:
            return i*j
        j += 1

ans = sieve()
print(ans)