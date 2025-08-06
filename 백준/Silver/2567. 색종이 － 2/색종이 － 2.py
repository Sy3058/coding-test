import sys
input = sys.stdin.readline

n = int(input())
board = [[False] * 101 for _ in range (101)]

for _ in range (n):
  x, y = map(int, input().split())
  for i in range (x, x+10):
    for j in range (y, y+10):
      board[i][j] = True # 색종이 영역 칠하기

ans = 0 # 둘레값
deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))

for i in range (101):
  for j in range (101):
    if board[i][j] == True:
      tmp = 0
      for dx, dy in deltas:
        if board[i+dx][j+dy] == True:
          tmp += 1
      # 해당하는 점의 4방향이 모두 1이 아니면 그 점은 둘레 값
      if tmp == 3: # 변의 길이
        ans += 1
      elif tmp == 2: # 모서리 점이므로 가로 세로 모두 존재
        ans += 2

print(ans)