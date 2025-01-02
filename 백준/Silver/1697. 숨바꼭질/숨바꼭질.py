import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

def bfs(s, t):
  nv = deque([s])
  visited = [False] * 100001 # 중복 작업 제거용 (현재 레벨의 모든 노드를 탐색하고 다음으로 넘어가므로 처음 도달하는 순간만 저장하면 됨)
  dis = [0] * 100001 # 각 위치까지의 이동 횟수 저장

  visited[s] = True

  while nv:
    x = nv.popleft()

    if x == t:
      return dis[x] # 타겟에 도달했을 때 이동 횟수를 반환
    
    for nx in (x+1, x-1, x*2):
      if 0 <= nx <= 100000 and not visited[nx]: # 범위 내이고 방문된 적 없는 경우
        visited[nx] = True
        dis[nx] = dis[x] + 1
        nv.append(nx)

ans = bfs(n, k)
print(ans)