import sys
input = sys.stdin.readline

n = int(input())
file = [list(input().strip()) for _ in range (n)]

if n == 1:
  print(''.join(file[0]))
else:
  target = file[0].copy()
  pattern = file[0].copy()

  for i in range (1, n):
    for j in range (len(file[0])):
      if target[j] != file[i][j]:
        pattern[j] = '?'

  print(''.join(pattern))