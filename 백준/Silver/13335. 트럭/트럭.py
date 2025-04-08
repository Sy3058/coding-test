import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
truck = list(map(int, input().split()))

bridge = deque([0]*(w-1) + [truck[0]]) # 다리에 올라가 있는 트럭
time = 1

for i in range (1, n):
  if sum(bridge) + truck[i] <= l: # 하중보다 작으면 트럭을 올림
    bridge.append(truck[i])
    bridge.popleft()
    time += 1
  
  else:    
    while sum(bridge) + truck[i] > l: # 트럭을 올릴 수 있을 때까지 나머지를 내보냄
      bridge.popleft()

      if sum(bridge) + truck[i] <= l: # 올릴 수 있어지면 올림
        bridge.append(truck[i])
        time += 1
        break

      else:
        bridge.append(0)
        time += 1

print(time + w)