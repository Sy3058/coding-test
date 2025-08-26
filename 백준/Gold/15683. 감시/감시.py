import sys
input = sys.stdin.readline

"""
5가지 CCTV
-> / <- -> / ㄴ / ㅗ / +
CCTV는 그 방향에 있는 칸 전체 감시, 벽 통과 불가, CCTV통과 가능, 회전 가능 (항상 90도 방향)
사각지대가 최소가 되는 크기?
"""

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range (N)]
cctv_pos = [] # cctv의 위치 및 모드를 저장할 변수
detected_walls = set()
for i in range (N):
  for j in range (M):
    if office[i][j] == 6:
      detected_walls.add((i, j))
    if office[i][j] in (1, 2, 3, 4, 5):
      cctv_pos.append((i, j, office[i][j])) # x좌표, y좌표, mode

modes = [
  [], # 0은 빈 칸
  [[0], [1], [2], [3]], # 1은 한 방향 (상 우 하 좌)
  [[0, 2], [1, 3]], # 2는 상하 / 좌우
  [[0, 1], [1, 2], [2, 3], [3, 0]], # 3은 ㄴ 방향
  [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]], # 4는 ㅗ 방향
  [[0, 1, 2, 3]] # 5는 전 방향
]

# 이동 방향 (상 우 하 좌)
mx = [0, 1, 0, -1]
my = [-1, 0, 1, 0]

def fill(x, y, deltas):
  detected = set([(x, y)]) # cctv 위치도 감시된 위치로 넣기
  for idx in deltas: # 4일 때 idx는 차례로 0, 1, 2, 3
    dx, dy = mx[idx], my[idx] # 감시할 방향
    cx, cy = x, y  # 방향마다 CCTV 원점에서 시작
    # 벽을 만나거나 사무실 크기를 넘어가면 종료
    while True:
      nx, ny = cx + dx, cy + dy
      if not (0 <= nx < N and 0 <= ny < M):
        break # 사무실 크기 넘어가면 종료
      if office[nx][ny] == 6:
        break # 벽을 만나면 종료
      detected.add((nx, ny))
      cx, cy = nx, ny # 다음 값을 현재 값으로 변경
  return detected

def backtrack(cctv_idx, total_detected):
  global max_detected
  if cctv_idx == len(cctv_pos):
    max_detected = max(max_detected, len(total_detected))
    return
  
  x, y, mode_idx = cctv_pos[cctv_idx] # x 좌표, y 좌표, mode
  mode = modes[mode_idx]

  for deltas in mode: # 감시할 방향
    detected = fill(x, y, deltas)
    backtrack(cctv_idx + 1, total_detected | detected) # 전체 감지된 범위에 현재 감지한 범위 추가

max_detected = 0
backtrack(0, detected_walls)

# 전체 크기에서 감지된 범위를 뺀 게 사각지대
print(N*M - max_detected)
