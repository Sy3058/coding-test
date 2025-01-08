import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range (n)]

# 산술 평균
print(round(sum(nums)/n))

# 중앙값
nums.sort()
print(nums[n//2])

# 최빈값
ctr = Counter(nums).most_common()
if len(ctr) > 1 and ctr[0][1] == ctr[1][1]:
  print(ctr[1][0])
else:
  print(ctr[0][0])

# 범위
print(nums[-1] - nums[0])