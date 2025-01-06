import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deq = deque()

def command(deq, c):
  if c[0] == 1:
    deq.appendleft(c[1])
  
  elif c[0] == 2:
    deq.append(c[1])
  
  elif c[0] == 3:
    if deq:
      print(deq.popleft())
    else:
      print(-1)
  
  elif c[0] == 4:
    if deq:
      print(deq.pop())
    else:
      print(-1)
  
  elif c[0] == 5:
    print(len(deq))
  
  elif c[0] == 6:
    if deq:
      print(0)
    else:
      print(1)
  
  elif c[0] == 7:
    if deq:
      print(deq[0])
    else:
      print(-1)
  
  else:
    if deq:
      print(deq[-1])
    else:
      print(-1)

for _ in range (n):
  c = list(map(int, input().split()))
  command(deq, c)