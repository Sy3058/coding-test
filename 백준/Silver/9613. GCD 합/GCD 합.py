import sys
import math
input = sys.stdin.readline

t = int(input())

for _ in range (t):
  data = input().split()
  n, *arr = map(int, data)
  hap = 0

  for i in range (n):
    for j in range (i + 1, n):
      hap += math.gcd(arr[i], arr[j])
  
  print(hap)