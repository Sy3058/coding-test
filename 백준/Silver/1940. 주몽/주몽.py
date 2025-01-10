import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
nums = list(map(int, input().split()))

cnt = 0

nums.sort()
s = 0
e = n-1

while s < e:
  if nums[e] + nums[s] < m:
    s += 1
  
  elif nums[e] + nums[s] > m:
    e -= 1
  
  else:
    cnt += 1
    s += 1
    e -= 1

print(cnt)