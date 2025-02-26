import sys
input = sys.stdin.readline

n = int(input())
i = 1
while n != 0:
  if n % 2 == 0:
    print('%d. even %d'%(i, n//2))
  else:
    print('%d. odd %d'%(i, n//2))
  i += 1
  n = int(input())