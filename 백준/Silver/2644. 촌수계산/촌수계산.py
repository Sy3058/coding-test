import sys
from collections import deque

n = int(sys.stdin.readline()) # 전체 사람 수
p1, p2 = map(int, sys.stdin.readline().split()) # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
m = int(sys.stdin.readline()) # 부모 자식들 간의 관계의 개수

graph = [[] for _ in range (n+1)]
visited = [False] * (n+1)
result = []

for _ in range (m):
  x, y = map(int, sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)

# bfs
def bfs(start, end):
  nv = deque([(start, 0)]) # (현재 노드, 촌수)
  visited[start] = True

  while nv:
    cur, cnt = nv.popleft()

    if cur == end: # 목표 노드에 도달한 경우
      return cnt
    
    for i in graph[cur]:
      if not visited[i]:
        visited[i] = True
        nv.append((i, cnt + 1))
  
  return -1 # 목표 노드에 도달하지 못한 경우

print(bfs(p1, p2))