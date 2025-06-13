import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
comp = {i:[] for i in range (1, n+1)}
dp = [0] * (n+1)

for _ in range (m):
  a, b = map(int, input().split())
  comp[b].append(a)

def bfs(s):
  nv = deque([s])
  cnt = 0
  visited[s] = 1

  while nv:
    x = nv.popleft()
    cnt += 1
    for i in comp[x]:
      if not visited[i]:
        nv.append(i)
        visited[i] = 1
  
  return cnt


for i in range (1, n+1):
  visited = [0] * (n+1)
  dp[i] = bfs(i)

mv = max(dp)

for i in range (1, n+1):
  if dp[i] == mv:
    print(i, end = ' ')