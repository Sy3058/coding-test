"""
서로 다른 색이 직사각형 모양 색종이 n장
각 색종이가 보이는 부분의 면적
=> board를 순회하며 board[i][j]를 n으로 갱신
"""
import sys
input = sys.stdin.readline

n = int(input())
board = [[0] * 1001 for _ in range (1001)]
area = dict()

for k in range (1, n+1):
  a, b, w, h = map(int, input().split())

  # (a, b)에서 너비 w, 높이 h인 사각형을 board에서 찾아서 그 값을 모두 k로 변경
  for i in range (a, a+w):
    for j in range (b, b+h):
      board[i][j] = k

# board에서 num을 찾아서 개수를 추가
for row in board:
  for num in row:
    area[num] = area.get(num, 0) + 1

for i in range (1, n+1):
  print(area[i])