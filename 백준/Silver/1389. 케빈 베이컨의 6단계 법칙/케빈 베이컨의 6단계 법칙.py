from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 친구 관계 저장 (ex. {1:[3, 4], 2:[3], ...})
fl = {i:[] for i in range (1, n+1)}
for _ in range (m):
    a, b = map(int, input().split())
    fl[a].append(b)
    fl[b].append(a)

# 각각의 케빈 베이컨 수를 저장할 리스트
ans = [0] * (n+1)

def bfs(s): # bfs는 최단 거리를 탐색
    v = [False] * (n + 1)
    dist = [0] * (n + 1) # i번째까지의 거리 계산
    nv = deque([s])
    v[s] = True

    while nv:
        x = nv.popleft()
        for nx in fl[x]: # x의 친구 탐색
            if not v[nx]:
                v[nx] = True
                dist[nx] = dist[x] + 1 # 
                nv.append(nx)
    return sum(dist)

min_sum = float('inf')
answer = 0

for i in range (1, n+1):
    total = bfs(i)
    if total < min_sum:
        min_sum = total
        answer = i

print(answer)