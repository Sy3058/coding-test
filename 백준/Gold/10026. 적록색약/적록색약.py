import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range (n)]
tfrg = [[True]*n for _ in range (n)]
tf = [[True]*n for _ in range (n)]
rg = ('R', 'G')
rgcnt = 0 # 적록색약인 사람이 볼 때
cnt = 0 # 적록색약이 아닌 사람이 볼 때

def dfsrg(s):
  nv = [s]
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  bs = arr[s[0]][s[1]]

  while nv:
    x, y = nv.pop()

    for dx, dy in directions:
      nx, ny = x+dx, y+dy

      if 0 <= nx < n and 0 <= ny < n and tfrg[nx][ny]:
        if bs in rg and arr[nx][ny] in rg:
          tfrg[nx][ny] = False
          nv.append((nx, ny))
        elif arr[nx][ny] == bs:
          tfrg[nx][ny] = False
          nv.append((nx, ny))

def dfs(s):
  nv = [s]
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  bc = arr[s[0]][s[1]] # base color

  while nv:
    x, y = nv.pop()

    for dx, dy in directions:
      nx, ny = x+dx, y+dy

      if 0 <= nx < n and 0 <= ny < n and tf[nx][ny] and arr[nx][ny] == bc:
        tf[nx][ny] = False
        nv.append((nx, ny))

for i in range (n):
  for j in range (n):
    if tfrg[i][j]:
      dfsrg((i, j))
      rgcnt += 1
      dfs((i, j))
      cnt += 1
    elif tf[i][j]:
      dfs((i, j))
      cnt += 1

print(cnt, rgcnt)