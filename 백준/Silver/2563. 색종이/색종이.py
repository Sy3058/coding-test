import sys

n = int(sys.stdin.readline())
paper = [[0] * 100 for _ in range (100)]
width = 0

for _ in range (n):
  x, y = map(int, sys.stdin.readline().split())
  for i in range (x, x+10):
    for j in range (y, y+10):
      paper[i][j] = 1

for a in range (100):
  width += paper[a].count(1)

print(width)
