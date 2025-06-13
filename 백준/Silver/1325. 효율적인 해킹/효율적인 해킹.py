import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
comp = {i:[] for i in range (1, n+1)}
dp = [0] * (n+1)

for _ in range (m):
  a, b = map(int, input().split())
  comp[a].append(b)

def bfs(s):
  nv = deque([s])
  visited[s] = 1

  while nv:
    x = nv.popleft()

    for i in comp[x]:
      if not visited[i]:
        visited[i] = 1
        nv.append(i)
        dp[i] += 1

for i in range (1, n+1):
  visited = [0] * (n+1)
  bfs(i)

mv = max(dp)

for i in range (1, n+1):
  if dp[i] == mv:
    print(i, end = ' ')