import sys
input = sys.stdin.readline

x1, y1, x2, y2, x3, y3 = map(int, input().split())

def check():
  # 세 점이 한 직선에 있는 경우
  if x1 == x2 == x3 or y1 == y2 == y3:
    return -1.0
  if x1 == x2:
    if (y3-y1)/(x3-x1) == (y3-y2)/(x3-x2):
      return -1.0
  elif x2 == x3:
    if (y3-y1)/(x3-x1) == (y2-y1)/(x2-x1):
      return -1.0
  else:
    if (y3-y2)/(x3-x2) == (y2-y1)/(x2-x1):
      return -1.0
  ab = ((x2-x1)**2 + (y2-y1)**2)**0.5
  bc = ((x3-x2)**2 + (y3-y2)**2)**0.5
  ac = ((x3-x1)**2 + (y3-y1)**2)**0.5
  abac = (ab + ac)*2
  abbc = (ab + bc)*2
  acbc = (ac + bc)*2
  return max(abs(abac - abbc), abs(abac-acbc), abs(abbc-acbc))

print(check())
