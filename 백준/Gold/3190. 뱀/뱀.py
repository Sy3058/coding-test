import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수
apple = set([tuple(map(int, input().split())) for _ in range (k)]) # 사과의 위치
l = int(input()) # 뱀의 방향 변환 횟수
red = {int(x): c for x, c in (input().split() for _ in range(l))} # 방향 변환 정보


def Dummy():
  board = [[False]*(n+1) for _ in range (n+1)]
  snake = deque([(1, 1)])
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  direction = 0
  cnt = 0 # 시간
  i = 0 # 방향 변환 확인

  while True:
    cnt += 1
    x, y = snake[-1]
    dx, dy = directions[direction]
    nx, ny = x+dx, y+dy
    if 1 <= nx <= n and 1 <= ny <= n and not board[nx][ny]:
      board[nx][ny] = True # 이동한 위치
      snake.append((nx, ny))
      if (nx, ny) not in apple: # 사과를 먹지 못하면 꼬리 이동
        lx, ly = snake.popleft()
        board[lx][ly] = False
      else: # 사과를 먹었다면 제거 
        apple.remove((nx, ny))

    else:
      return cnt

    if cnt in red:
      if red[cnt] == 'L': # 반시계 방향 회전
        direction = (direction - 1) % 4
      else: # 시계 방향 회전
        direction = (direction + 1) % 4

print(Dummy())