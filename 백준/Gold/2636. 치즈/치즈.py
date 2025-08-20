r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range (r)]
deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))

def dfs(x, y, target_cheese):
  nv = [(x, y)]

  while nv:
    cx, cy = nv.pop()

    for dx, dy in deltas:
      nx, ny = cx + dx, cy + dy

      if not (0 <= nx < r and 0 <= ny < c):
        continue

      if visited[nx][ny]:
        continue
      
      # 다음 위치가 공기라면 nv에 넣고 치즈라면 target_cheese에 넣기
      if board[nx][ny] == 0:
        nv.append((nx, ny))
        visited[nx][ny] = True
      
      else:
        target_cheese.add((nx, ny))
        visited[nx][ny] = True
  
  # 아직 녹을 치즈가 있는 경우
  if target_cheese:
    return True
  
  # 더 이상 치즈가 없는 경우
  else:
    return False

cnt = 0
while True:
  visited = [[False] * c for _ in range (r)]
  target_cheese = set()
  if dfs(0, 0, target_cheese):
    cnt += 1
    cheese = len(target_cheese)
    for tx, ty in target_cheese: # target인 치즈를 녹이기
      board[tx][ty] = 0
  else:
    break

# target_cheese가 있을 때만 cheese를 갱신하므로 저장되어 있는 cheese가 마지막 치즈
print(f"{cnt}\n{cheese}")
