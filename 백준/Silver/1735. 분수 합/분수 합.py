import sys

def gcd(a, b): # 두 수의 최대 공약수
  while b > 0:
    a, b = b, a % b
  return a

a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

num = a1 * b2 + a2 * b1 # 분자
den = b1 * b2 # 분모

g = gcd(num, den)
print(num//g, den//g)