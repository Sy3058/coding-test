import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

qn = a.count(0) # 큐의 개수
ans = []

if m > qn:
  for i in range (n-1, -1, -1):
    if a[i] == 0: ans.append(b[i])
  ans.extend(c[:m-qn])
else:
  for i in range (n-1, -1, -1):
    if a[i] == 0: ans.append(b[i])
    if len(ans) == m: break

print(*ans)