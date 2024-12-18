import sys
from collections import deque

n = int(sys.stdin.readline())
tree = [[] for _ in range (n+1)]

# a와 b를 각각의 tree에 연결해줌
for _ in range (n-1):
  a, b = map(int, sys.stdin.readline().split())
  tree[a].append(b)
  tree[b].append(a)

# 부모 노드
parent = [0] * (n+1)

# BFS
def bfs():
  deq = deque([1]) # 루트 노드는 1
  while deq:
    c = deq.popleft()
    for t in tree[c]:
      if parent[t] == 0: # 방문되지 않은 노드
        parent[t] = c # 현재 노드를 부모로 설정
        deq.append(t)

bfs()

for i in range (2, n+1):
  print(parent[i])
