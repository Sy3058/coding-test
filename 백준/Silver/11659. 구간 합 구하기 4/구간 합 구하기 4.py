import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
ps = [] # 누적 합
hap = 0
for i in range (n):
  hap += num[i]
  ps.append(hap)

for _ in range (m):
  i, j = map(int, input().split())
  if i == 1:
    print(ps[j-1])
  else:
    print(ps[j-1] - ps[i-2]) # j까지의 합에서 i-1까지의 합을 빼면 i부터 j까지의 합