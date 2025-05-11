import sys
input = sys.stdin.readline

t = int(input())

def gcd(a, b): # 최대 공약수 구하는 방법
  while b > 0:
    a, b = b, a % b
  return a

for _ in range (t):
  data = input().split()
  n, *arr = map(int, data)
  hap = 0

  for i in range (n):
    for j in range (i + 1, n):
      hap += gcd(arr[i], arr[j])
  
  print(hap)