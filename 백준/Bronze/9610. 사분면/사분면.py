n = int(input())
q1, q2, q3, q4, axis = 0, 0, 0, 0, 0

for _ in range (n):
  x, y = map(int, input().split())
  if x == 0 or y == 0:
    axis += 1
  elif x > 0 and y > 0:
    q1 += 1
  elif x < 0 and y > 0:
    q2 += 1
  elif x < 0 and y < 0:
    q3 += 1
  else:
    q4 += 1

print('Q1: %d'%(q1))
print('Q2: %d'%(q2))
print('Q3: %d'%(q3))
print('Q4: %d'%(q4))
print('AXIS: %d'%(axis))