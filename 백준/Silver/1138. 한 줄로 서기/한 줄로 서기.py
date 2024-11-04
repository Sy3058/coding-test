import sys

N = int(sys.stdin.readline()) # 사람의 수
order = list(map(int, sys.stdin.readline().split())) # 자기보다 키 큰 사람이 왼쪽에 몇명이나 있는지
ans = [0] * N

for i in range (1, N+1):
  idx = order[i-1]
  cnt = 0
  for j in range (N):
    if cnt == idx and ans[j] == 0:
      ans[j] = i
      break
    if ans[j] == 0: # i보다 키 큰 사람의 명수
      cnt += 1

print(' '.join(map(str,ans)))