import sys

N = int(sys.stdin.readline())
arr = []
visited = [[False]*N for _ in range (N)]

for _ in range (N):
  row = list(map(int, sys.stdin.readline().split()))
  arr.append(row)

def dfs():
  directions = [(1,0), (0,1)] # 오른쪽이나 아래로만 이동 가능
  nv = [(0,0)]
  flag = True

  while nv:
    x, y = nv.pop()
    visited[x][y] = True
    for dx, dy in directions:
      num = arr[x][y] 
      nx, ny = x+dx*num, y+dy*num
      if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
        nv.append((nx, ny))
      if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == -1: # 끝 점에 도달한 경우
        nv = [] # while 조건 break
        flag = False
        break # for문 break
  
  print('Hing' if flag else 'HaruHaru')

dfs()