import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
v = [-1] * 100001

def bfs(s, t):
  nv = deque([s])
  v[s] = 0

  while nv:
    x = nv.popleft()
    
    if x == t:
      return v[x]
    
    if 0 <= x*2 <= 100000 and v[x*2] == -1:
      v[x*2] = v[x]
      nv.appendleft(x*2)
    
    for nx in (x-1, x+1):
      if 0 <= nx <= 100000 and v[nx] == -1:
        v[nx] = v[x] + 1
        nv.append(nx)

print(bfs(n, k))