import sys

ds = []

for _ in range (3):
  d = int(sys.stdin.readline())
  ds.append(d)

if set(ds) == {60}:
  print('Equilateral')

elif sum(ds) == 180 and len(set(ds)) == 2:
  print('Isosceles')

elif sum(ds) == 180:
  print('Scalene')

else:
  print('Error')