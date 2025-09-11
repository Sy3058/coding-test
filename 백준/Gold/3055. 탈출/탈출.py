from collections import deque

r, c = map(int, input().split())
board = []
nv = deque()
# visited에 방문한 시간을 저장
visited = [[-1] * c for _ in range (r)]

# D: 비버의 굴, S: 고슴도치 위치
for i in range (r):
  line = list(input().strip())
  board.append(line)
  for j in range (c):
    if line[j] == "*":
      nv.appendleft((i, j, "*")) # 물부터 탐색
      visited[i][j] = 0
    
    elif line[j] == "S":
      start = (i, j)

# 고슴도치 위치를 마지막으로 탐색
nv.append((start[0], start[1], "H")) # x, y, hedgehog (고슴도치의 위치)
visited[start[0]][start[1]] = 0

deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))

def sol():
  while nv:
    x, y, state = nv.popleft()
    time = visited[x][y]

    # 고슴도치가 목적지에 도착하면 time return
    if state == "H" and board[x][y] == "D":
      print(time)
      return
    
    for dx, dy in deltas:
      nx, ny = x + dx, y + dy

      # 범위 밖이면 지나가기
      if not (0 <= nx < r and 0 <= ny < c):
        continue
      
      if visited[nx][ny] == -1 and board[nx][ny] != "X":
        # 벽이 아니고 방문한 적 없을 때
        if state == "H":
          if board[nx][ny] == "D" or board[nx][ny] == ".":
            nv.append((nx, ny, "H"))
            visited[nx][ny] = time + 1
        
        else: # state == "*"
          if board[nx][ny] == "." or board[nx][ny] == "H":
            nv.append((nx, ny, "*"))
            visited[nx][ny] = time + 1
            board[nx][ny] = "*" # 물 퍼트리기
    
  print("KAKTUS")

sol()