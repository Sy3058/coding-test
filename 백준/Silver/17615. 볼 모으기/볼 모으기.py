import sys
input = sys.stdin.readline

n = int(input())
balls = list(input().strip())

def solution():
  # 전체 R과 B의 개수
  nr = balls.count('R')
  nb = n - nr

  if nr == n or nr == 0:
    return 0

  # 첫 R과 B의 위치
  fr = balls.index('R')
  fb = balls.index('B')

  # 마지막 R과 B의 위치
  i = n-1
  lr = 0
  lb = 0
  while balls[i] == balls[-1]:
    if balls[-1] == 'B':
      lr += 1
    else:
      lb += 1
    i -= 1

  if balls[0] == balls[-1]:
    if balls[0] == 'R':
      a = nr - max(fb, lb)
    else:
      a = nb - max(fr, lr)

  else:
    a = min(nb - max(fr, lr), nr - max(fb, lb))

  a = min(a, nb, nr)
  return a

print(solution())