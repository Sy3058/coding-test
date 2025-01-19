import sys
input = sys.stdin.readline

t = int(input())
for _ in range (t):
  x, y = map(int, input().split())
  dis = y - x
  n = int(dis ** 0.5)
  if n**2 + n > dis:
    n -= 1

  rest = dis - (n**2 + n)

  if rest == 0:
    print(2*n)

  elif rest <= n+1:
    print(2*n + 1)

  else:
    print(2*n + 2)