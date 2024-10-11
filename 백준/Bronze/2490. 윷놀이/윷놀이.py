for _ in range (3):
  yut = input().split()
  c = yut.count('0')
  if c == 1:
    print('A')
  elif c == 2:
    print('B')
  elif c == 3:
    print('C')
  elif c == 4:
    print('D')
  else:
    print('E')