import sys
input = sys.stdin.readline

def is_prime(x): # 밀러-라빈 알고리즘
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

t = int(input()) # test case

for _ in range (t):
  n = int(input())
  if n <= 2:
    print(2)
    continue
  while not is_prime(n): # n이 소수가 될 때까지 1씩 더하면서 확인
    n += 1
  print(n)