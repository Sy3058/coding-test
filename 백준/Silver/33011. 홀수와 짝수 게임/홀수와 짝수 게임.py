import sys
input = sys.stdin.readline

t = int(input())
for _ in range (t):
  n = int(input())
  A = list(map(int, input().split()))
  even, odd = 0, 0
  for i in range (n):
    if A[i]%2:
      odd += 1
    else:
      even += 1

  a = max(odd, even)
  b = min(odd, even)

  if a%2 and a != b:
    print('amsminn')
  else:
    print('heeda0528')
