import sys

input = sys.stdin.readline

n, m, b = map(int, input().split()) # 세로, 가로, 블럭 개수

height_counts = {} # 높이별로 개수 저장

for _ in range(n):

  for height in map(int, input().split()):

    height_counts[height] = height_counts.get(height, 0) + 1

min_time = float('inf')

max_height = 0

# 현재 존재하는 높이를 순서대로 정렬

heights = sorted(height_counts.keys())

for target in range (257): # 가능한 모든 높이 탐색

  remove_blocks = 0

  add_blocks = 0

  # 사용한 블럭 계산

  for h in heights:

    cnt = height_counts[h] # 현재 높이에 해당하는 위치의 개수

    if h == target:

      continue

    if h > target: # 현재 높이가 타겟보다 높으면 블럭 제거

      remove_blocks += (h - target) * cnt

    else:

      add_blocks += (target - h) * cnt

  

  # 인벤토리 내의 블럭보다 사용해야할 블럭이 많으면 다음으로

  if b + remove_blocks < add_blocks:

    continue

  

  # 제거 2초 생성 1초

  t = remove_blocks * 2 + add_blocks

  # 최소 시간, 최대 높이

  if t < min_time or (t == min_time and target > max_height):

    min_time = t

    max_height = target

print(min_time, max_height)