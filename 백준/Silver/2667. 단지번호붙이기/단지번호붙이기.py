import sys

n = int(sys.stdin.readline())
arr = []
visited = [[False] * n for _ in range (n)]
villages = []

for _ in range (n):
  a = list(sys.stdin.readline().strip())
  arr.append(a)

def dfs(x1, y1):
  nv = [(x1, y1)]
  cnt = 0 # 단지내 집의 수

  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  
  while nv:
    x, y = nv.pop()
    visited[x][y] = True
    cnt += 1

    for dx, dy in directions:
      nx, ny = x+dx, y+dy

      if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == '1' and visited[nx][ny] == False and (nx, ny) not in nv: # 범위 안에 집이 있으면서 방문되지 않은 경우
        nv.append((nx, ny))
  
  return cnt

for i in range (n):
  for j in range (n):
    if arr[i][j] == '1' and visited[i][j] == False:
      num = dfs(i, j)
      villages.append(num)

print(len(villages))
villages.sort()
for k in range (len(villages)):
  print(villages[k])