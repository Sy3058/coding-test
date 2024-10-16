import sys
from collections import deque

n, q = map(int, sys.stdin.readline().split()) # n: node 개수 q: 질문 개수
arr = [[] for _ in range(n+1)]

# 배열 구성
for _ in range (n-1):
  v1, v2, r = map(int, sys.stdin.readline().split())
  arr[v1].append((v2, r))
  arr[v2].append((v1, r))

# BFS 탐색 함수
def bfs(k, v):
  deq = deque([v])
  visited = [False] * (n+1)
  visited[v] = True
  cnt = 0

  while deq:
    current = deq.popleft()
    for neighbor, usado in arr[current]:
      if not visited[neighbor] and usado >= k:
        visited[neighbor] = True
        deq.append(neighbor)
        cnt += 1
  return cnt

for _ in range (q):
  k, v = map(int, input().split())
  print(bfs(k, v))