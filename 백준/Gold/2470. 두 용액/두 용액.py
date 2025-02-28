import sys
input = sys.stdin.readline

n = int(input())
cs = list(map(int, input().split())) # characteristic
cs.sort()
l = 0
r = n-1
tch = float('inf') # 두 용액의 합

while l < r:
  tmp = cs[l] + cs[r]
  if tmp == 0: # 0일 때가 무조건 최소이므로 break
    ans = (cs[l], cs[r])
    break
  if abs(tmp) < tch: # 두 용액의 합이 최소일 때 정답 갱신
    ans = (cs[l], cs[r])
    tch = abs(tmp)
  if abs(cs[l]) > abs(cs[r]): # 절대값이 더 큰 값을 줄여야 함
    l += 1
  else:
    r -= 1

print(*ans)