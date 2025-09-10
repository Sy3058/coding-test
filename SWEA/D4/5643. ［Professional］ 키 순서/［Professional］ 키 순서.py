from collections import deque

def bfs(s, is_small):
  visited = [False] * (n+1)
  nv = deque()

  cnt = 0
  visited[s] = True
  nv.append(s)

  while nv:
    cur = nv.pop()

    if is_small: # s보다 작은 사람 탐색
      for nxt in bgraph[cur]: # bgraph는 cur보다 작은 사람들
        if not visited[nxt]:
          visited[nxt] = True
          nv.append(nxt)
          cnt += 1
    else: # s보다 큰 사람 탐색
      for nxt in sgraph[cur]: # sgraph는 cur보다 큰 사람들
        if not visited[nxt]:
          visited[nxt] = True
          nv.append(nxt)
          cnt += 1
  
  return cnt

for tc in range (1, int(input()) + 1):
  n = int(input())
  m = int(input())
  sgraph = {i:[] for i in range (1, n + 1)} # i보다 []에 있는 사람이 큼
  bgraph = {i:[] for i in range (1, n + 1)} # i보다 []에 있는 사람이 작음

  for _ in range (m):
    # a의 키보다 b의 키가 큼
    a, b = map(int, input().split())
    sgraph[a].append(b) # a보다 큰 사람들
    bgraph[b].append(a) # b보다 작은 사람들
  
  ans = 0
  for i in range (1, n + 1):
    smaller = bfs(i, True) # i보다 작은 사람의 수
    bigger = bfs(i, False) # i보다 큰 사람의 수

    # i보다 작은 사람과 i보다 큰 사람을 더했을 때 n-1이면 모든 사람과 키 비교가 가능
    if (smaller + bigger == n - 1):
      ans += 1
    
  print(f"#{tc} {ans}")