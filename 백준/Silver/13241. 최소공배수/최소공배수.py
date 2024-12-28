import sys

def gcd(a, b): # 두 수의 최대 공약수
  while b > 0:
    a, b = b, a % b
  return a

def lcm(a, b): # 최소공배수 = 두 수의 곱 / 최대 공약수
  return a * b // gcd(a, b)

a, b = map(int, sys.stdin.readline().split())
print(lcm(a, b))