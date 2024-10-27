from collections import deque
import sys

n = int(sys.stdin.readline()) # number of command
queue = deque()

for _ in range (n):
  com = list(sys.stdin.readline().split())
  
  if com[0] == 'push':
    queue.append(int(com[1]))
  
  elif com[0] == 'pop':
    if queue:
      num = queue.popleft()
      print(num)
    else:
      print(-1)
  
  elif com[0] == 'size':
    print(len(queue))
  
  elif com[0] == 'empty':
    if queue: # 비어있지 않을 때
      print(0)
    else: # 비어있을 때
      print(1)
  
  elif com[0] == 'front':
    if queue:
      print(queue[0])
    else:
      print(-1)
  
  else: # if com[0] == 'back'
    if queue:
      print(queue[-1])
    else:
      print(-1)