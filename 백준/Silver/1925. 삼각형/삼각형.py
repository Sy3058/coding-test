import sys

x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
x3, y3 = map(int, sys.stdin.readline().split())
  
answers = ['X', 'JungTriangle', 'Dunkak2Triangle', 'Jikkak2Triangle', 'Yeahkak2Triangle', 'DunkakTriangle', 'JikkakTriangle', 'YeahkakTriangle']

# length ** 2
l12 = (x1-x2)**2 + (y1-y2)**2
l23 = (x2-x3)**2 + (y2-y3)**2
l31 = (x3-x1)**2 + (y3-y1)**2

# l123[2]가 가장 긴 변
l123 = list((l12, l23, l31))
l123.sort()

# 삼각형 넓이 공식
s = (x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x3*y2 + x2*y1)

if x1 == x2 == x3 or y1 == y2 == y3 or s == 0: # 세 점이 일직선
  print(answers[0])
elif l12 == l23 == l31: # 세 변의 길이가 동일
  print(answers[1])
elif l12 == l23 or l23 == l31 or l31 == l12: # 두 변의 길이가 동일
  if l123[2] > l123[0] + l123[1]:
    print(answers[2])
  elif l123[2] == l123[0] + l123[1]:
    print(answers[3])
  else:
    print(answers[4])
else: # 세 변의 길이가 모두 다름
  if l123[2] > l123[0] + l123[1]:
    print(answers[5])
  elif l123[2] == l123[0] + l123[1]:
    print(answers[6])
  else:
    print(answers[7])