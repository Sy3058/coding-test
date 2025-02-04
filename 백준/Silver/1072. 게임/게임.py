import sys
input = sys.stdin.readline

x, y = map(int, input().split())

def sol(x, y):
  z = y*100 // x
  if z >= 99:
    return -1
  
  a, b = 1, x
  while a <= b:
    c = (a+b)//2
    nz = (y+c)*100 // (x+c)
    if nz > z:
      b = c-1
    else:
      a = c+1
  return a

print(sol(x, y))