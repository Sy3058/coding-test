import sys

input = sys.stdin.readline
n = int(input()) # 수의 개수
nums = list(map(int, input().split())) # n개의 수
m = int(input()) # 구간의 개수
ijs = [tuple(map(int, input().split())) for _ in range (m)]

# 누적합 계산
prefix = [nums[i] for i in range (n)]
for i in range (1, n):
  prefix[i] += prefix[i-1]

# 이때 1 <= j, j <= N
for i, j in ijs:
  if i - 2 < 0:
    print(prefix[j-1])
  else:
    print(prefix[j-1] - prefix[i-2])