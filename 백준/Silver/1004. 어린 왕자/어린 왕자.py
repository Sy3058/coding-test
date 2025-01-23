import sys
input = sys.stdin.readline

# 내부에 시작점 혹은 끝점을 포함하는 행성을 찾아야함
t = int(input())

for _ in range (t):
  x1, y1, x2, y2 = map(int, input().split())
  n = int(input())
  cnt = 0
  for __ in range (n):
    cx, cy, r = map(int, input().split())
    d1 = ((cx-x1)**2 + (cy-y1)**2)**0.5
    d2 = ((cx-x2)**2 + (cy-y2)**2)**0.5
    if d1 < r and d2 < r: # 시작점과 끝점이 모두 원 내부에 존재하면 진입/이탈하지 않음
      continue
    elif d1 < r:
      cnt += 1
    elif d2 < r:
      cnt += 1

  print(cnt)