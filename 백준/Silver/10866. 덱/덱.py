import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque()

for _ in range (n):
  c = list(sys.stdin.readline().split())

  if c[0] == 'push_front':
    deq.appendleft(int(c[1]))
  
  elif c[0] == 'push_back':
    deq.append(int(c[1]))
  
  elif c[0] == 'pop_front':
    print(deq.popleft()) if deq else print(-1)
  
  elif c[0] == 'pop_back':
    print(deq.pop()) if deq else print(-1)
  
  elif c[0] == 'size':
    print(len(deq))
  
  elif c[0] == 'empty':
    print(0) if deq else print(1)
  
  elif c[0] == 'front':
    print(deq[0]) if deq else print(-1)

  elif c[0] == 'back':
    print(deq[-1]) if deq else print(-1)