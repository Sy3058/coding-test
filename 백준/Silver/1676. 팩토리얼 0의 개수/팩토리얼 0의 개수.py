import sys
input = sys.stdin.readline

def f(n):
  if n <= 1:
    return 1
  return n * f(n-1)

n = int(input())
num = f(n)
cnt = 0
while num%10 == 0:
  num //= 10
  cnt += 1

print(cnt)