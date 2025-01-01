import sys
input = sys.stdin.readline

def is_prime(x):
  for i in range(2, int(x**0.5) + 1): # 제곱근까지만 확인하면 됨
    if x % i == 0:
      return False
  return True # 나누어떨어지지 않았을 경우 소수

t = int(input()) # test case

for _ in range (t):
  n = int(input())
  if n <= 2:
    print(2)
    continue
  while not is_prime(n): # n이 소수가 될 때까지 1씩 더하면서 확인
    n += 1
  print(n)