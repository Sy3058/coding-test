import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
pop = list(list(map(int, input().split())) for _ in range (n))
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
dfsvisited = [[False] * n for _ in range (n)]

# find union
def bfs(s, visited):
  nv = deque([s])
  union = set([s]) # make index list of union
  up = pop[s[0]][s[1]] # union population
  visited[s[0]][s[1]] = True
  
  while nv:
    x, y = nv.popleft()

    for dx, dy in directions:
      nx, ny = x + dx, y + dy

      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
        if l <= abs(pop[nx][ny] - pop[x][y]) <= r:
          up += pop[nx][ny]
          nv.append((nx, ny))
          union.add((nx, ny))
          visited[nx][ny] = True
  
  np = up // len(union) # new population of union
  for x, y in union:
    pop[x][y] = np

  return len(union) > 1

days = 0
while True:
  movement = False
  visited = [[False] * n for _ in range (n)]

  for i in range (n):
    for j in range (n):
      if not visited[i][j]:
        if bfs((i, j), visited):
          movement = True
  
  if not movement:
    break

  days += 1
          
print(days)