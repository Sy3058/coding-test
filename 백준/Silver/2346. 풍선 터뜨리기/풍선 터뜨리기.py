import sys
from collections import deque

n = int(sys.stdin.readline())
balloons = list(map(int, sys.stdin.readline().split()))

bs = deque((i + 1, num) for i, num in enumerate(balloons)) # 풍선 번호와 값을 덱에 저장
result = []

while bs:
  index, value = bs.popleft() # 첫 번째 위치에 있는 풍선을 터트림
  result.append(index)

  if value > 0: # 풍선이 터지면서 이미 오른쪽으로 한 칸 이동된 상태이므로 한 칸 덜 움직여야 함
    bs.rotate(-value+1)
  else:
    bs.rotate(-value)

print(' '.join(map(str, result)))