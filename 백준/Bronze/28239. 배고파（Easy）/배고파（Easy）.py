import sys
input = sys.stdin.readline

n = int(input())
for _ in range (n):
  flag = False
  m = int(input())
  for i in range (61):
    for j in range (i, 61):
      if 2**i + 2**j == m:
        print(i, j)
        flag = True
        break
    if flag:
      break