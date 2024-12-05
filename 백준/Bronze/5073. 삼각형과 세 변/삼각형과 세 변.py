import sys

a, b, c = map(int, sys.stdin.readline().split())

while a+b+c != 0:
  l = [a, b, c]
  l.sort()
  sl = set(l)

  if l[2] >= l[0] + l[1]:
    print('Invalid')

  elif len(sl) == 1:
    print('Equilateral')
  
  elif len(sl) == 2:
    print('Isosceles')
  
  else:
    print('Scalene')

  a, b, c = map(int, sys.stdin.readline().split())