from collections import deque

n, m = map(int, input().split()) # 미로의 세로 크기, 가로 크기
maze = [list(input().strip()) for _ in range (n)]

# 시작 위치 찾기
for i in range (n):
  for j in range (m):
    if maze[i][j] == '0':
      sp = (i, j) # start point
      maze[i][j] = '.' # 다시 방문하게될 수도 있으므로

deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))
# visited[x][y][key_bitmask] 형태로 저장
visited = [[[False] * 64 for _ in range (m)] for _ in range (n)]

nv = deque()
nv.append((sp[0], sp[1], 0, 0)) # x, y, key_bitmask, 이동횟수
visited[sp[0]][sp[1]][0] = True # 키가 없는 상태에서 방문처리

while nv:
  x, y, keys, cnt = nv.popleft()

  # 목적지에 도착했다면 (bfs이므로 일단 도착하면 그게 최소)
  if maze[x][y] == '1':
    print(cnt)
    break

  for dx, dy in deltas:
    nx, ny = x + dx, y + dy

    if 0 <= nx < n and 0 <= ny < m:
      cell = maze[nx][ny] # 다음 칸에 있는 값
      nxt_keys = keys

      # 벽이면 지나갈 수 없음
      if cell == "#":
        continue
      
      # 문일 경우 열쇠가 없으면 못 감
      if "A" <= cell <= "F":
        # A를 기준으로 A~F의 인덱스 계산
        # cell에 해당하는 키가 없으면 다음으로
        if not (keys & (1 << (ord(cell) - ord("A")))):
          continue
      
      # 열쇠일 경우 키 추가
      if 'a' <= cell <= 'f':
        nxt_keys |= (1 << (ord(cell) - ord('a')))
      
      # 완성된 상태로 방문한 적 없다면
      if not visited[nx][ny][nxt_keys]:
        visited[nx][ny][nxt_keys] = True
        nv.append((nx, ny, nxt_keys, cnt + 1))

else: # 루프가 break 없이 정상 종료되었을 때 == cnt가 출력된 적 없을 때
  print(-1)