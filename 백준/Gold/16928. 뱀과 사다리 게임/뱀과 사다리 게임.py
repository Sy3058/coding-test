import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
move = {}
dp = [0] * (101)

for _ in range (n+m):
  s, e = map(int, input().split()) # x to y
  move[s] = e

def bfs():
  nv = deque([(1, 0)]) # position, count

  dice = (1, 2, 3, 4, 5, 6)

  while nv:
    p, cnt = nv.popleft()
    
    for d in dice:
      np = p + d # next position

      if np == 100:
        return cnt + 1

      if np > 100:
        continue

      if np in move:
        np = move[np]
      
      if dp[np] != 0:
        continue

      nv.append((np, cnt+1))
      dp[np] = cnt + 1


print(bfs())