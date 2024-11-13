import sys
from collections import deque

nums = deque(sys.stdin.readline().strip())
n = 0

while nums: # nums에 수가 존재하는 동안
  n += 1
  num = deque(str(n))
  while num and nums: # num과 nums에 모두 수가 존재하는 동안
    if num[0] == nums[0]: # 1의 자리가 일치하면 nums에서 첫번째 수 제거
      nums.popleft()
    num.popleft() # 일치하지 않아도 num에서는 계속 첫번째 수 제거

print(n)