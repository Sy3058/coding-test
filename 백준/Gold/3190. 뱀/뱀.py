import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수
apple = set([tuple(map(int, input().split())) for _ in range (k)]) # 사과의 위치
l = int(input()) # 뱀의 방향 변환 횟수
red = [tuple(input().split()) for _ in range (l)] # 방향 변환 정보

board = [[False]*(n+1) for _ in range (n+1)]
snake = deque([(1, 1)])
d = [0, 1] # 현재 방향
cnt = 0 # 시간
i = 0 # 방향 변환 확인

def change_direction(d): # 방향 전환
  if d[0] == 0:
    if red[i][1] == 'L': d[0], d[1] = -d[1], d[0]
    else: d[0], d[1] = d[1], d[0]
  else:
    if red[i][1] == 'L': d[0], d[1] = d[1], d[0]
    else: d[0], d[1] = d[1], -d[0]

while True:
  cnt += 1
  x, y = snake[-1]
  nx, ny = x+d[0], y+d[1]
  if 1 <= nx <= n and 1 <= ny <= n and not board[nx][ny]:
    board[nx][ny] = True # 이동한 위치
    snake.append((nx, ny))
    if (nx, ny) not in apple: # 사과를 먹지 못하면 꼬리 이동
      lx, ly = snake.popleft()
      board[lx][ly] = False
    else: # 사과를 먹었다면 제거 
      apple.remove((nx, ny))

  else:
    break

  if i < len(red) and cnt == int(red[i][0]): # 방향 변환
    change_direction(d)
    i += 1

print(cnt)