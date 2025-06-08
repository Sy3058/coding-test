import sys
input = sys.stdin.readline

n = int(input())
fl = [] # 시작점
tl = [] # 도착점

def move(n, s, e):
  mid = 6 - s - e

  if n == 1:
    fl.append(s)
    tl.append(e)
  
  else:
    move(n-1, s, mid)
    fl.append(s)
    tl.append(e)
    move(n-1, mid, e)

move(n, 1, 3)
print(len(fl))

for i in range (0, len(fl)):
  print("%d %d" %(fl[i], tl[i]))