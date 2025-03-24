import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
ladder = {} # move from x to y (upward)
snake = {} # move from u to v (downward)
dp = [0] * (101)

for _ in range (n):
  x, y = map(int, input().split()) # x to y
  ladder[x] = y

for _ in range (m):
  u, v = map(int, input().split())
  snake[u] = v

def bfs():
  nv = deque([(1, 0)]) # position, count

  dice = (1, 2, 3, 4, 5, 6)

  while nv:
    p, cnt = nv.popleft()
    
    for d in dice:
      np = p + d # next position

      if np == 100:
        return cnt+1
      
      if np < 100 and dp[np] == 0: # not visited and np in board
        if np in ladder:
          np = ladder[np]
        
        elif np in snake:
          np = snake[np]
        
        nv.append((np, cnt+1))
        dp[np] = cnt


print(bfs())