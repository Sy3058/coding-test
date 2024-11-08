import sys

n, m = map(int, sys.stdin.readline().split())
pic = []
visited = [([False] * m) for _ in range (n)]

for _ in range (n):
  row = list(map(int, sys.stdin.readline().split()))
  pic.append(row)

max_size = 0 # 그림의 최대 넓이
cnt = 0 # 그림의 개수

def dfs(x, y):
  nv = [(x, y)] # need visited
  size = 0 # 그림의 넓이

  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  while nv:
    x, y = nv.pop()
    visited[x][y] = True
    size += 1

    for dx, dy in directions:
      nx = x + dx
      ny = y + dy

      if 0 <= nx < n and 0 <= ny < m and pic[nx][ny] == 1 and visited[nx][ny] == False: # 범위 내에 있으면서 그림이 있고 방문된 적 없는 경우
        nv.append((nx, ny))
        visited[nx][ny] = True
  
  return size
        
for i in range (n):
  for j in range (m):
    if pic[i][j] == 1 and visited[i][j] == False:
      tmp_size = dfs(i, j)
      cnt += 1

      if tmp_size > max_size:
        max_size = tmp_size

print(cnt)
print(max_size)